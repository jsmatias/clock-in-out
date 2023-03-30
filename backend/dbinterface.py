import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

load_dotenv("../.env")


class Interface:

    def __init__(self) -> None:
        self.hostname = os.getenv("HOSTNAME")
        self.user = os.getenv("USER")
        self.pw = os.getenv("PASSWORD")
        self.dbName = "timelog"

        self.createDbConnection()

    def createDbConnection(self):
        self.connection = None
        try:
            self.connection = mysql.connector.connect(
                host=self.hostname,
                user=self.user,
                passwd=self.pw,
                database=self.dbName
            )
            print("MySQL Database connection successful")
        except Error as err:
            print(f"Error: '{err}'")

    def executeQuery(self, query):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            self.connection.commit()
            print("Query successful")
        except Error as err:
            print(f"Error: '{err}'")
