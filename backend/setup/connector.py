import mysql.connector
from mysql.connector import Error

SUCCESS = True
ERROR = False


def createServerConnection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


def executeQuery(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        return ({"success": SUCCESS, "msg": "Query Successful"})
    except Error as err:
        return ({"success": ERROR, "msg": f"Error: '{err}'"})


def createDatabase(connection, dbName):
    createDbQuery = f"CREATE DATABASE {dbName}"
    res = executeQuery(connection, createDbQuery)
    if res['success']:
        print("Database created successfully")
    else:
        print(res["msg"])


def createTable(connection, createTableQuery):

    res = executeQuery(connection, createTableQuery)
    if res['success']:
        print(f"Table created successfully")
    else:
        print(res["msg"])
