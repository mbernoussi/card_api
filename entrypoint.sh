#!/bin/sh
source ./venv/bin/activate
gunicorn -b :8080 card_api.apis:app