"""Testing of env_manipulation.py

NB: Not built for asynchronous testing
"""

from unittest import TestCase
import sys
from dotenv import set_key, dotenv_values

import app.functions.constants as c

sys.path.append(c.FUNCTIONS_APP)
from app.functions.env_manipulation import ENVManipulator
import app.tests.data_env_manipulation as d


class ENVManipulatorTest(TestCase):
    def test_init(self):
        ENVManipulator(c.TESTING_ENV_PATH_MKDOCS)

    def test_delete(self):
        # Clears out the contents
        open(c.TESTING_ENV_PATH_MKDOCS, "w").close()
        set_key(c.TESTING_ENV_PATH_MKDOCS, "key1", d.VALUE1)
        set_key(c.TESTING_ENV_PATH_MKDOCS, "key2", d.VALUE2)
        em = ENVManipulator(c.TESTING_ENV_PATH_MKDOCS)
        self.assertTrue(em.delete("key1"))
        self.assertTrue(em.delete("key2"))

    def test_delete_key_not_present(self):
        # Clears out the contents
        open(c.TESTING_ENV_PATH_MKDOCS, "w").close()
        set_key(c.TESTING_ENV_PATH_MKDOCS, "key1", d.VALUE1)
        em = ENVManipulator(c.TESTING_ENV_PATH_MKDOCS)
        self.assertFalse(em.delete("wrong_key"))

    # TODO - needs writing
    def test_delete_all(self):
        pass

    def test_add(self):
        # Clears out the contents
        open(c.TESTING_ENV_PATH_MKDOCS, "w").close()
        em = ENVManipulator(c.TESTING_ENV_PATH_MKDOCS)
        em.add("key1", d.VALUE1)
        dot_values = dotenv_values(c.TESTING_ENV_PATH_MKDOCS)
        self.assertEqual(d.VALUE1, dot_values.get("key1"))

    def test_read(self):
        # Clears out the contents
        open(c.TESTING_ENV_PATH_MKDOCS, "w").close()
        set_key(c.TESTING_ENV_PATH_MKDOCS, "key1", d.VALUE1)
        em = ENVManipulator(c.TESTING_ENV_PATH_MKDOCS)
        self.assertEqual(d.VALUE1, em.read("key1"))

    def test_read_all(self):
        # Clears out the contents
        open(c.TESTING_ENV_PATH_MKDOCS, "w").close()
        # Adds out of order to check return string is in alphabetical order
        set_key(c.TESTING_ENV_PATH_MKDOCS, "key1", d.VALUE1)
        set_key(c.TESTING_ENV_PATH_MKDOCS, "key3", d.VALUE3)
        set_key(c.TESTING_ENV_PATH_MKDOCS, "key2", d.VALUE2)
        em = ENVManipulator(c.TESTING_ENV_PATH_MKDOCS)
        self.assertEqual(em.read_all(), d.READ_ALL_RETURN)
