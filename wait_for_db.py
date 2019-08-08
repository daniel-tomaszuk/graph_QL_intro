import logging
import os
from time import sleep
from time import time

import psycopg2

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())

check_timeout = os.getenv("POSTGRES_CHECK_TIMEOUT", 10)
check_interval = os.getenv("POSTGRES_CHECK_INTERVAL", 5)
interval_unit = "second" if check_interval == 1 else "seconds"

start_time = time()

db_kwargs = dict(
    dbname=os.getenv('POSTGRES_DB'),
    user=os.getenv('POSTGRES_USER'),
    password=os.getenv('POSTGRES_PASSWORD'),
    host=os.getenv('POSTGRES_HOST'),  # IMPORTANT: it should be name of the DB service from docker-compose
    port=os.getenv('POSTGRES_PORT')
)


def check_db():
    while time() - start_time < check_timeout:
        try:
            conn = psycopg2.connect(**db_kwargs)
            logger.info("Postgres is ready!")
            conn.close()
            return True
        except psycopg2.OperationalError as e:
            logger.info(
                'Postgres isn\'t ready. Waiting for %s %s...',
                check_interval,
                interval_unit
            )
            logger.error('Error: %s, with: %s', e, db_kwargs)
            sleep(check_interval)

    logger.error(
        'We could not connect to Postgres within %s seconds.',
        str(check_timeout + interval_unit)
    )
    return False


if __name__ == '__main__':
    check_db()
