import mysql
from mysql.connector import Error

try:
    server_connection = mysql.connector.connect(
        host='localhost',
        port='3306',
        user='root',
        charset='utf8',
        password='root',
        database='',
    )
    print('connected to server successfully')

    # if server_connection.is_connected():
    #     print('I AM HERE')
    #     server_state=True
    # db_Info = server_connection.get_server_info()
    # print("Connected to MySQL Server version ", db_Info)

    server_cursor = server_connection.cursor()
    # sql_cursor.execute("select database();")
    # record = sql_cursor.fetchone()

except Error as e:
    print(e)