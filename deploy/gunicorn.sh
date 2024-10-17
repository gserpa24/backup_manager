#!/bin/bash

NAME="backup_manager"
DJANGODIR=$(dirname $(cd `dirname $0` && pwd))
SOCKFILE=/tmp/gunicorn-bk.sock
LOGDIR=${DJANGODIR}/logs/gunicorn.log
USER=serpa
GROUP=serpa
NUM_WORKERS=4
DJANGO_WSGI_MODULE=backup_manager.wsgi

rm -frv $SOCKFILE

echo $DJANGODIR

cd $DJANGODIR

exec ${DJANGODIR}/env/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
  --log-file=$LOGDIR