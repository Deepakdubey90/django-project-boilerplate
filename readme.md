#NewCo

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
npm install
bower install
psql -c 'create database newco'
python manage.py syncdb
python manage.py migrate
python manage.py collectstatic
python manage.py runserver
```

## Issues and Pull Requests:

Feel free to log any issues here https://github.com/vinitkumar/newco/issues.
If you wish to contribute, fork and send a pull request.

## Warning
This is purely meant for learning purpose and by no means is
going to be stable and should be expected to break all the time.
