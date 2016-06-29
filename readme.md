# Django Project Boilerplate

[![Build Status](https://travis-ci.org/vinitkumar/django-project-boilerplate.svg?branch=master)](https://travis-ci.org/vinitkumar/django-project-boilerplate)

[![Coverage Status](https://coveralls.io/repos/github/vinitkumar/django-project-boilerplate/badge.svg?branch=master)](https://coveralls.io/github/vinitkumar/django-project-boilerplate?branch=master)

The project is an example of using latest cutting edge and supported technology. I wrote it for myself to experiment
with a Python-3.5.0 project and has all good things included such as test coverage and builds with travis and coveralls.

I am using bower to maintain frontend libraries/frameworks. Django rest framework for APIs.

## Installation

Following are the installation instructions:

```sh
git clone git@github.com:vinitkumar/django-project-boilerplate.git
cd django-project-boilerplate
export PROJECT_NAME='django-project-boilerplate'
mkvirtualenv $PROJECT_NAME -r requirements.txt
setvirtualenvproject
npm install
bower install
psql -c 'create database newco'
workon $PROJECT_NAME
python manage.py migrate
python manage.py collectstatic
python manage.py runserver
```

## Deployment to Heroku

Apply following steps:

- Add a postgres and pgbackups (free tier) to your dyno.
- Add heroku remote to your git. `git remote add heroku git://heroku.com/app.git`
- Add this buildpack (`heroku config:set
  BUILDPACK_URL='git://github.com/heroku/heroku-buildpack-python.git'`).
  This is very important as heroku will read package.json file and consider it
  a node.js app.
- Just do your changes and push code to heroku remote like: `git push heroku
  HEAD:master`


## Code Quality

Use Pylint with pylint-django plugin:

```
pylint --load-plugins pylint_django views.py
```

## Issues and Pull Requests:

Feel free to log any issues here https://github.com/vinitkumar/django-project-boilerplate/issues
If you wish to contribute, fork and send a pull request.

## Warning
This is purely meant for learning purpose and by no means is
going to be stable and should be expected to break all the time.
