import sqlite3
import mysql.connector
from mysql.connector import Error
import pyodbc
import functions as my_fnc


def db_connection():
    try:
        sqliteConnection = sqlite3.connect('data.db')
        cursor = sqliteConnection.cursor()

    except sqlite3.Error as error:

        print("Error while connecting to sqlite", error)

    return sqliteConnection, cursor


def db_connection_server(server, host, port, user, passwd, dbname):

    server_cursor = None
    server_connection = None
    if server == "MySQL":

        try:
            server_connection = mysql.connector.connect(
                host=host,
                port=port,
                user=user,
                charset='utf8',
                password=passwd,
                database=dbname,
            )

            # if server_connection.is_connected():
            #     print('I AM HERE')
            #     server_state=True
            # db_Info = server_connection.get_server_info()
            # print("Connected to MySQL Server version ", db_Info)

            server_cursor = server_connection.cursor()
            # sql_cursor.execute("select database();")
            # record = sql_cursor.fetchone()

        except Error as e:
            my_fnc.db_errors(str(e))

    else:

        try:

            server_connection = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                                               "Server=" + host + ";"
                                               "UID="+user+";"
                                               "PWD="+passwd+";"                                             
                                               "Database="+dbname+";"
                                               "Trusted_Connection=no;"
                                               )

            server_cursor = server_connection.cursor()

        except pyodbc.Error as e:
            my_fnc.db_errors(str(e))

    return server_connection, server_cursor
