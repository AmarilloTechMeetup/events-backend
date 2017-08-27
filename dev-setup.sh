#!/bin/bash
# This is a quick setup script for developers working on
# the project.
#
# This assumes that the user is root on an Ubuntu 16.04 instance.
# This has been tested primarily on Digital Ocean with their smallest droplet.
# It should work with a few tweaks just about anywhere.
#
# Based on an example by Rohini Choudhary 
# at: https://jee-appy.blogspot.com/2017/01/deply-django-with-nginx.html
#
# TODO: convert this to use environment variables for production

# install everything we need
apt-get update
apt-get -y install
apt-get -y install postgresql postgresql-contrib
apt-get -y install python-virtualenv
apt-get -y install libpq-dev python3-dev
apt-get -y install supervisor
apt-get -y install nginx

# setup the database as user postgres (added by apt-get above)
su - postgres -c 'createuser -D -S -R db_user'
su - postgres -c "psql -c \"ALTER USER db_user WITH PASSWORD 'db_user';\""
su - postgres -c 'createdb --owner db_user django_db'

# setup the django user
adduser --disabled-password --gecos "" django

# setup site as django user

# setup virtual env
su - django -c 'virtualenv -p python3 django_env'

# install django
su - django -c 'source ~/django_env/bin/activate && pip install django'
su - django -c 'source ~/django_env/bin/activate && pip install psycopg2'

# clone the repository
su - django -c 'git clone https://github.com/AmarilloTechMeetup/events-backend.git'

# install dependencies	
su - django -c 'source ~/django_env/bin/activate && cd /home/django/events-backend/app && pip install -r requirements.txt'

# run the migrations

su - django -c 'source ~/django_env/bin/activate && cd /home/django/events-backend/app && python manage.py migrate'


# install gunicorn
su - django -c 'source ~/django_env/bin/activate && pip install gunicorn'

# setup logs
su - django -c 'mkdir -p /home/django/logs/'
su - django -c 'touch /home/django/logs/gunicorn_supervisor.log'

# setup supervisor
cp /home/django/events-backend/etc/supervisor/conf.d/events-backend.conf /etc/supervisor/conf.d/events-backend.conf
chown root.root /etc/supervisor/conf.d/events-backend.conf

systemctl restart supervisor
systemctl enable supervisor

# setup nginx
cp /home/django/events-backend/etc/nginx/sites-available/events-backend.conf /etc/nginx/sites-available/events-backend.conf
chown root.root /etc/nginx/sites-available/events-backend.conf
ln -s /etc/nginx/sites-available/events-backend.conf /etc/nginx/sites-enabled/events-backend.conf
rm /etc/nginx/sites-enabled/default

service nginx restart
