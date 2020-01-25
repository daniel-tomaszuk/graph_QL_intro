from django.db.models import Prefetch
from rest_framework import viewsets

from api.v1.REST.serializers import SatelliteSerializer
from f2f_Q3_2019 import settings
from tracker.models import Position
from tracker.models import Satellite
from tracker.utils import get_tz_time_period


class SatellitePositionsView(viewsets.ModelViewSet):
    TIMEZONE_KEY = "HTTP_X_CLIENT_TIMEZONE"
    serializer_class = SatelliteSerializer

    def get_queryset(self):
        prefetch = Prefetch("positions", to_attr="satellite_positions")
        query_params = self.request.query_params.get("query", "")
        client_tz = self.request.META.get(self.TIMEZONE_KEY, "")
        timezone = client_tz or settings.TIME_ZONE

        if query_params and query_params.lower() != "all":
            # prepare query param - make it uppercase and snake case it
            query_params = query_params.upper().replace("-", "_")
            # filter query
            try:
                from_datetime_local, to_datetime_local = get_tz_time_period(
                    query_params, timezone
                )

                prefetch = Prefetch(
                    "positions",
                    queryset=Position.objects.filter(
                        timestamp__gte=from_datetime_local,
                        timestamp__lte=to_datetime_local,
                    ).order_by("-timestamp"),
                    to_attr="satellite_positions",
                )
            except KeyError:
                pass

        queryset = Satellite.objects.all().prefetch_related(prefetch)
        return queryset
