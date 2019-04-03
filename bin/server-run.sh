#!/usr/bin/env  bash
PORT=$1

if [ "$PORT" = "" ]; then
	PORT='8000'
fi

bin/run.sh runserver 0.0.0.0:$PORT