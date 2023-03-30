import unittest
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv("../.env")

# Tests:
#   1. Connection
#   2. DB creation (check existing db with same name, create new)
#   3. Connection do DB
#   4. Create table (check for existing table, create a new)
#   5. Insert new entry row value


class TestConnection(unittest.TestCase):
    """Oracle MySQL for Python Connector tests."""

    connection = None

    def setUp(self):
        config = dict(
            user=os.getenv("USER"),
            password=os.getenv("PASSWORD"),
            host=os.getenv("HOSTNAME"),
            database="timelog",
        )
        self.connection = mysql.connector.connect(**config)

    def tearDown(self):
        if self.connection is not None and self.connection.is_connected():
            self.connection.close()

    def test_connection(self):
        self.assertTrue(self.connection.is_connected())


if __name__ == '__main__':
    unittest.main()
