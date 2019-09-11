#!/bin/bash
flask db upgrade
#flask translate compile
flask run --host=0.0.0.0 --port=8000
#exec gunicorn -b :8000 --access-logfile - --error-logfile - app:app
