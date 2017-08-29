# Amarillo Event Hub Backend

This repository is a Django backend for the Amarillo Event Hub project, a collaborative, Make-a-thon hack built
by a team of volunteers over the evening of August 11, 2017.

This will be an open source project, as soon as we agree on a license.

The front end for this project is [also on GitHub] (https://github.com/AmarilloTechMeetup/events-frontend)

## Contributing

If you want to help with the project, just fork it on GitHub and send us a pull request.

## Quickstart

[![Dply](https://dply.co/b.svg)](https://dply.co/b/AbLM1dqg) 

Connect to the server then

```
su - django
```
Seriously, that's it.

You have two hours free, or you can pay a couple bucks for a day long coding session, or you can commit/push and click the button again.

## Manual Setup 

To setup a dev environment for the back end on your own server:

+ Spin-up an Ubuntu 16.04 instance on your favorite cloud host.
+ Connect to the instance as root
+ Run the setup script:

```

curl 'https://raw.githubusercontent.com/AmarilloTechMeetup/events-backend/master/dev-setup.sh' | bash

```

or if you want to be really clever and are using a cloud provider that supports cloud script


```
#cloud-config

runcmd:
  -  curl 'https://raw.githubusercontent.com/AmarilloTechMeetup/events-backend/master/dev-setup.sh' | bash

```

+ Once the script completes you can test that that your setup is working by visiting http://{YOUR IP ADDRESS}/api/event/


## Now what?

The good bits will be in /home/django/events-backend/app.

The backend stack is niginx -> gunicorn -> django -> postgresql.

## Warnings and Disclaimers

> You'll shoot your eye out kid! - Santa

This is very much a work in progress and providing a place for people to learn and share their work is as important as building a good site.

Please email bill@billglover.com if you were at the Make-a-thon and would like to be added to the CONTRIBUTORS file.

