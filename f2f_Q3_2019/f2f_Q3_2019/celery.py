from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'f2f_Q3_2019.settings')

app = Celery('f2f_Q3_2019')
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

# add celery beat config
app.conf.beat_schedule = {
    'get_satellites_positions': {
        'task': 'core.tasks.get_satellite_positions',
        'schedule': crontab(minute='*'),
        'args': (),
    },
}
