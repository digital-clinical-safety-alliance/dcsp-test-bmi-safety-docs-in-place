""" Constants

Forward slash '/' is placed at the end of directory names
"""
from enum import Enum

MAIN_FOLDER: str = "/bmi-calc/"
TESTS_LOCATION: str = f"{ MAIN_FOLDER }app/bmi-calc/app/tests/"

ILLEGAL_DIR_CHARS: str = '<>?:"\\|?*,'

# Functions within django app
FUNCTIONS_APP: str = f"{ MAIN_FOLDER }app/bmi-calc/app/functions/"


# .env
ENV_PATH = f"{ MAIN_FOLDER }.env"


# .env manipulation for placeholders
ENV_PATH_PLACEHOLDERS = f"{ MAIN_FOLDER }.env_placeholders"


# testing Django
TESTING_ENV_PATH_DJANGO: str = (
    f"{ TESTS_LOCATION }test_django/.env_placeholders_test"
)

FORM_ELEMENTS_MAX_WIDTH: str = "max-w-800"
