#!/bin/bash

cd /bmi-calc/app
python3 env_startup_check.py

# Check the exit code of env checker
if [ $? -ne 0 ]; then
  exit 1
fi

#cd /bmi-calc/app/bmi-calc
#python3 manage.py runserver 0.0.0.0:8000 &

# Black linter
echo Running Black linter
cd /bmi-calc/app
black . --line-length=79 --check

# Check the exit code of the linter
if [ $? -ne 0 ]; then
  echo "Black linter failed!"
  exit 1
fi

# Check for security issues with Bandit
echo "Checking for security issues"
cd /bmi-calc/app
bandit -c bandit.yml -r .

# Check the exit code of the linter
if [ $? -ne 0 ]; then
  echo "Bandit security checker failed!"
  exit 1
fi

# Run type checking using mypy (replace with your type-checking command)
echo "Running type checking..."
cd /bmi-calc/app
mypy /bmi-calc/app/bmi-calc/app/

# Check the exit code of the type checking command
if [ $? -ne 0 ]; then
  echo "Type checking failed!"
  exit 1
fi

# Run unit tests using pytest (replace with your unit testing command)
echo "Running unit tests..."
cd /bmi-calc/app/bmi-calc
python3 -u manage.py test --settings=bmi-calc.settings_tests --exclude-tag=git

# Check the exit code of the unit testing command
if [ $? -ne 0 ]; then
  echo "Unit testing failed!"
  exit 1
fi

# If all tests pass, the exit with 0
echo "Tests passed successfully!"
exit 0