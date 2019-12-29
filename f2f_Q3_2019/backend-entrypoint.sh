#!/bin/bash
python wait_for_db.py
python manage.py migrate
python manage.py collectstatic --no-input
gunicorn -w 5 --bind 0.0.0.0:8000 --forwarded-allow-ips='*' f2f_Q3_2019.wsgi --log-level DEBUG
