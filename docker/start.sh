#!/bin/bash
while true; do
    flask db upgrade
    if [[ "$?" == "0" ]]; then
        break
    fi
    echo Upgrade command failed, retrying in 5 secs...
    sleep 5
done
#flask translate compile
flask run --host=0.0.0.0 --port=8000
#exec gunicorn -b :8000 --access-logfile - --error-logfile - app:app
