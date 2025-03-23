#!/bin/bash

rm db.sqlite3
rm -rf ./callerapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations callerapi
python3 manage.py migrate callerapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens

