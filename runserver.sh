#!/bin/sh

/usr/local/bin/python /usr/local/canvasser-leaflet/manage.py collectstatic
/usr/local/bin/python /usr/local/canvasser-leaflet/manage.py runserver 0:8000
