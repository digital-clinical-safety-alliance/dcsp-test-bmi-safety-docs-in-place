"""Testing of env_manipulation.py

Can be async
"""

from unittest import TestCase
import sys
import app.functions.constants as c

sys.path.append(c.FUNCTIONS_APP)
from app.functions.email_functions import EmailFunctions


class EmailFunctionsTest(TestCase):
    def test_valid_email(self):
        email_function = EmailFunctions()
        self.assertTrue(email_function.valid_syntax("abc.def@hig.com"))

    def test_invalid_email(self):
        email_function = EmailFunctions()
        self.assertFalse(email_function.valid_syntax("123"))
