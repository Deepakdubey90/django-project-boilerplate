# Based on http://codeinthehole.com/writing/continuously-re-build-your-project/
build: clean virtualenv database


# cleanup
clean:
	-find . -type f -name "*.pyc" -delete
	-rm -rf static
	-rm -rf media

# Add and update the virtualenv
virtualenv:
	pip install -r requirements.txt

database:
	psql -c 'create database newco'
	python manage.py migrate

backup:
	pg_dump -h localhost -d newco > ~/newco.sql

test:
	python manage.py test -v2

dropdb:
	dropdb newco

cleandb: backup dropdb database


