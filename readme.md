#NewCo

[![Build
Status](https://travis-ci.org/vinitkumar/newco.svg)](https://travis-ci.org/vinitkumar/newco)

NewCo is a Django app boilerplate with good configuration. If you have
a Django based backend that interacts with Client Side MVC or if you
have a app that renders everything from backend, it would help you in both
cases.


## Installation

Following are the installation instructions:

```sh
git clone git@github.com:vinitkumar/newco.git
cd newco
export PROJECT_NAME='newco'
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

Feel free to log any issues here https://github.com/vinitkumar/newco/issues.
If you wish to contribute, fork and send a pull request.

## Warning
This is purely meant for learning purpose and by no means is
going to be stable and should be expected to break all the time.
