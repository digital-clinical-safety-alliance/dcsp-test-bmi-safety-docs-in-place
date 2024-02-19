#!/bin/bash

trap 'exitFunction' EXIT

exitFunction() {
    exit 0
}

cd /bmi-calc/app
python3 env_startup_check.py

# Check the exit code of env checker
if [ $? -ne 0 ]; then
  exit 1
fi


cd /bmi-calc/app/bmi-calc
python3 manage.py runserver 0.0.0.0:8000 &

while :
do
    ((count++))
    sleep 1
done