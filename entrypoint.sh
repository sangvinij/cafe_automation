#!/bin/bash
python cafe/manage.py migrate
python cafe/manage.py runserver 0.0.0.0:8000
