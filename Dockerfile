FROM python:3-alpine

# RUN wget -O /tmp/gdal-2.3.1.tar.gz 'http://download.osgeo.org/gdal/2.3.1/gdal-2.3.1.tar.gz'

RUN apk update
RUN apk add uwsgi uwsgi-logfile uwsgi-python3 uwsgi-syslog 
RUN apk add gcc musl-dev 
RUN apk add su-exec
RUN apk add postgresql-dev
# to compile GDAL
# RUN apk add g++ make linux-headers
RUN apk add --no-cache --virtual .crypto-rundeps \
  --repository http://dl-cdn.alpinelinux.org/alpine/edge/main \
  libressl2.7-libcrypto

RUN apk add --no-cache --virtual .build-deps-testing \
  --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing \
  gdal-dev 

RUN apk add libxml2-dev libxslt-dev

RUN apk add --no-cache --virtual .build-deps-testing \
  --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing \
  geos-dev 

RUN pip3 install "Django==2.0.4" "django-floppyforms==1.7.0" "django-geojson==2.11.0" "django-leaflet==0.23.0" "psycopg2-binary==2.7.4" "pytz==2018.4" "six==1.11.0"
RUN pip3 install "geos"

# uwsgi stuff
COPY uwsgi.ini /etc
COPY uwsgi-foreground.sh /

RUN mkdir -p /usr/local/canvasser-leaflet/hvdsa
RUN mkdir -p /usr/local/canvasser-leaflet/canvasser
COPY hvdsa /usr/local/canvasser-leaflet/hvdsa
COPY canvasser /usr/local/canvasser-leaflet/canvasser
COPY manage.py /usr/local/canvasser-leaflet/
COPY hvdsasecrets.py /usr/local/canvasser-leaflet/
