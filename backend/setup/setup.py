from dotenv import load_dotenv
import connector
import os
from schema import timeEntriesSchema

load_dotenv("../.env")
hostname = os.getenv("HOSTNAME")
user = os.getenv("USER")
pw = os.getenv("PASSWORD")


def main():

    dbName = 'timelog'
    connection = connector.createServerConnection(
        hostname, user, pw)

    connector.createDatabase(connection, dbName)
    connector.createTable(connection, timeEntriesSchema)


if __name__ == '__main__':
    main()
