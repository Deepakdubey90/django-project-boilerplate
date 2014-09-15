##############################
Welcome to Newco Documentation
##############################

Installation
============

Install Save The Change just like everything else:

.. code-block:: bash

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


Usage
=====

And that's it! Keep using Django like you always have, Save The Change will take
care of you.


How It Works
============

Some text

Goodies
=======

Some more text

Developer Interface
===================

.. automodule:: apps.posts.models
	:members: Posts
	:undoc-members:

