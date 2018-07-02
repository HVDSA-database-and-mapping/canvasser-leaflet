#!/bin/sh

rsyslogd

uwsgi --ini /etc/uwsgi.ini
