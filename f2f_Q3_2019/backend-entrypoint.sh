#!/bin/bash
python wait_for_db.py
python manage.py migrate
python manage.py collectstatic --no-input
gunicorn -c './gunicorn.conf.py' f2f_Q3_2019.wsgi --log-level DEBUG
