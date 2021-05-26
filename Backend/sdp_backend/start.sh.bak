#!/bin/sh
dockerize -wait tcp://db:5432 -timeout 20s

python manage.py makemigrations
python manage.py migrate

gunicorn --preload sdp_backend.asgi:application -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000

# python manage.py runserver 0.0.0.0:8000
