from celery.utils.log import get_task_logger

from f2f_Q3_2019.celery import app as celery_app

logger = get_task_logger(__name__)


@celery_app.task()
def debug_task():
    logger('Task fired')
