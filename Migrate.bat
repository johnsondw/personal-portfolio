@echo off
cls
python manage.py makemigrations
python manage.py migrate
