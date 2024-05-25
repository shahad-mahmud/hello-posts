#! /bin/bash

set -e

MODULE_NAME=app.main

HOST=0.0.0.0
PORT=8000

exec uvicorn --host $HOST --port $PORT --reload $MODULE_NAME:app
