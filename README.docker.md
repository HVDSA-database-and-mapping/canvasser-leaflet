In order to make this app into a docker container, take these steps:

1. Copy `hvdsasecrets.example.py` to `hvdsasecrets.py` and change the values.

2. Run the command:

    docker build -t canvasser-leaflet .

3. Start a postgis container, with:

    docker run --name canvasser-postgis -d -e POSTGRES_PASSWORD=<some-cool-password> mdillon/postgis:10-alpine

4. Start the canvasser app, with:

    docker run --name canvasser -d --link canvasser-postgis:postgres canvasser-leaflet

**NOTE** that the container is still under development, so the canvasser container won't start uwsgi automatically.  For development, I instead run it as an interactive container:

    docker run --name canvasser -it --rm --link canvasser-postgis:postgres canvasser-leaflet /bin/sh

In the container, I do:

    # cd /usr/local/canvasser-leaflet
    # python manage.py runserver 0.0.0.0:8000
