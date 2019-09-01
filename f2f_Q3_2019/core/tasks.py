import json
import logging
from json import JSONDecodeError
from typing import Dict, List

import requests
from rest_framework import status

from f2f_Q3_2019.celery import app as celery_app
from f2f_Q3_2019.settings import N2YO_API_KEY_V1, N2YO_BASE_URL_V1
from tracker.models import Satellite, Position

logger = logging.getLogger(__name__)

BASE_ALTITUDE = 135
BASE_LATITUDE = 53.13333
BASE_LONGITUDE = 23.15

ISS_NORAD_ID = 25544

NORAD_IDS_TO_FIND = [
    ISS_NORAD_ID
]


@celery_app.task
def get_satellite_positions():
    """
    GET Request: /positions/{id}/{observer_lat}/{observer_lng}/{observer_alt}/{seconds}
    Gets satellite positions as described here: https://www.n2yo.com/api/#positions
    Creates new Satellite object (if required) and links position to it.
    """
    seconds_to_check = 1
    url = N2YO_BASE_URL_V1 \
        + f'positions/{ISS_NORAD_ID}/{BASE_LATITUDE}/{BASE_LONGITUDE}/{BASE_ALTITUDE}/{seconds_to_check}' \
        + f'&apiKey={N2YO_API_KEY_V1}'
    logger.debug('Send request to N2YO for satellites positions: %s', url)
    response = requests.get(url)

    try:
        response_data: Dict = json.loads(response.content)
        logger.debug('Dumped response into JSON.')

    except JSONDecodeError as e:
        logger.error('Got error during parsing JSON response: %s', e)
        return

    if response.status_code == status.HTTP_200_OK and 'error' not in response_data:
        logger.debug('Starting to process the response')

        # look for satellite and append position for it
        satellite_info: Dict = response_data.get('info')
        satellite_position: List = response_data.get('positions')
        if satellite_info and satellite_position:
            norad_id = satellite_info['satid']
            satellite_data = dict(
                name=satellite_info['satname'],
                norad_id=norad_id,
            )
            satellite, _ = Satellite.objects.get_or_create(
                norad_id=norad_id,
                defaults=satellite_data
            )
            satellite_positions_to_link = []
            for sat_position in satellite_position:
                satellite_positions_to_link.append(
                    Position(
                        satellite=satellite,
                        latitude=sat_position.get('satlatitude'),
                        longitude=sat_position.get('satlongitude'),
                        altitude=sat_position.get('sataltitude'),
                        azimuth=sat_position.get('azimuth'),
                        elevation=sat_position.get('elevation'),
                        ra=sat_position.get('ra'),
                        dec=sat_position.get('dec'),

                        observer_altitude=BASE_ALTITUDE,
                        observer_latitude=BASE_LATITUDE,
                        observer_longitude=BASE_LONGITUDE
                        )
                )
            Position.objects.bulk_create(satellite_positions_to_link)
            logger.debug('Created new Satellite positions')
            return

    logger.error('Got error response: %s', response_data)
    return
