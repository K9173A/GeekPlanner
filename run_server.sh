#!/bin/bash
# This script is intended to start a specific server type.
# How to run:
# chmod u+x run_server.sh
# ./run_server.sh [development | production]

source venv/bin/activate
cd GeekPlanner

if [[ "$1" == "development" ]];
then
    echo "Starting development server..."
    export GEEKPLANNER_DEVELOPMENT=true
    python manage.py runserver 0.0.0.0:8000
elif [[ "$1" == "production" ]];
then
    echo "Starting production server..."
else
    echo "Error: invalid value!"
    echo "Use 'development' or 'production' value for server type!"
fi
