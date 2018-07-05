"""This file contains the secrets to use in an installation of the app.

These secrets should not be used in production.  Instead, you should copy this file to hvdsa/secrets.py and change the values.

If you're using docker, you can use --volume to mount your secrets file in place.
"""
import os

SECRET_KEY = '05f31bgo)^ymwvy@ztxoim)ndp2p-*b8al__a579coma33i4w('

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'hvdsa',
        'USER': 'rwturner',
    }
}
