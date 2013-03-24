django-pug
==========

Django project for running a Python User Group


Getting Started
===============

The project is meant to be run from a virtualenv

git clone https://github.com/jlujan/django-pug.git

virtualenv --no-site-packages ./django-pug

cd django-pug

source bin/activate

pip install -r requirements.pip

export PYTHONPATH=./src:$PYTHONPATH

export DEVELOPMENT=1

cd src

python manage.py syncdb

python manage.py runserver
