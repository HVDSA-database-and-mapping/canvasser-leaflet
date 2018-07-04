In order to make this app into a docker container, take these steps (most of this is about getting the database set up, and only needs to be done once):

1. Copy `hvdsasecrets.example.py` to `hvdsasecrets.py` and change the values.

2. Run the command:

    docker build -t turfcutter /path/to/turfcutter

3. Start a postgis container, with:

    docker run --name turfcutter-postgis -d -e POSTGRES_PASSWORD=<some-cool-password> mdillon/postgis:10-alpine

4. Obtain a copy of the database backup.  The database backup can be found on the HVDSA google drive.  It is called `hvdsa_db.bkp`

5. Import the database backup into your postgis database:

    docker run -it --rm --link turfcutter-postgis:postgres --volume /path/to/hvdsa_db.bkp:/usr/share/hvdsa_db.bkp postgres:10-alpine pg_restore -h postgres -U postgres -d postgres /usr/share/hvdsa_db.bkp
    # (you'll have to enter your some-cool-password when prompted)

6. Set the search path.  You will only need to do this once per database-import.

    docker run -it --rm --link turfcutter-postgis:postgres postgres:10-alpine psql -h postgres -U postgres postgres -c  'ALTER DATABASE postgres SET search_path TO "$user", public, tiger, hvdsa, tiger_data, topology;'

7. Start the turfcutter app, with:

    docker run -it --rm --name turfcutter --link turfcutter-postgis:postgres turfcutter

This runs turfcutter using django's "runserver".  It is suitable for development.  If we want to use docker in production, we should make a version of the container that uses uwsgi, and run it in conjunction with an nginx container.


Now you are ready to develop.  If you make changes, you can stop the running container (with a ^C) and rebuild it.

    docker build -t turfcutter /path/to/turfcutter
    docker run --name turfcutter -it --rm --link turfcutter-postgis:postgres turfcutter
