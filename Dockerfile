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

RUN apk add jpeg-dev

RUN pip3 install pipenv
COPY Pipfile /usr/local/canvasser-leaflet/
COPY Pipfile.lock /usr/local/canvasser-leaflet/
RUN cd /usr/local/canvasser-leaflet && pipenv install --system

RUN apk add postgresql-client

# uwsgi stuff
COPY uwsgi.ini /etc
COPY uwsgi-foreground.sh /

RUN mkdir -p /usr/local/canvasser-leaflet/hvdsa
RUN mkdir -p /usr/local/canvasser-leaflet/turfcutter
RUN mkdir -p /usr/local/canvasser-leaflet/templates
RUN mkdir -p /usr/local/canvasser-leaflet/static
COPY hvdsa /usr/local/canvasser-leaflet/hvdsa
COPY turfcutter /usr/local/canvasser-leaflet/turfcutter
COPY templates /usr/local/canvasser-leaflet/templates
COPY static /usr/local/canvasser-leaflet/static

COPY manage.py /usr/local/canvasser-leaflet/
COPY hvdsasecrets.py /usr/local/canvasser-leaflet/

WORKDIR /usr/local/canvasser-leaflet

CMD ["/usr/local/bin/python", "manage.py", "runserver", "0:8000"]
