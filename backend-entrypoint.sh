#!/bin/bash
python ./wait_for_db.py
python ./$MANAGEDIR/manage.py migrate
python ./$MANAGEDIR/manage.py collectstatic --no-input
python ./$MANAGEDIR/manage.py runserver 0.0.0.0:8000
