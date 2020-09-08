import os, re
import sqlite3

script = ""
path = r'C:\Users\Billy\Desktop\versions'


def db_connection():
    try:
        sqliteConnection = sqlite3.connect('data.db')
        cursor = sqliteConnection.cursor()

    except sqlite3.Error as error:

        print("Error while connecting to sqlite", error)

    return sqliteConnection, cursor


sqliteConnection, cursor = db_connection()

version_names_list = os.listdir(path)
# print(version_names_list)
for version_name in version_names_list:
    version_dir_path = os.path.join(path, version_name)

    for subdir, dirs, files in os.walk(version_dir_path):

        if re.search(".*(\\\mysql)$", subdir) is not None:

            for filename in os.listdir(subdir):
                filepath = os.path.join(subdir, filename)

                with open(filepath, 'r') as f:
                    lines = f.readlines()

                    for line in lines:
                        clean_line = line.rstrip()
                        if not clean_line.startswith('-') and not clean_line.startswith('/'):
                             script += clean_line

                    # insert query here
                    try:

                        insert_script_query = """INSERT INTO Mysql_Scripts(name_version, script) values(?,?);"""
                        val = (version_name, script)
                        cursor.execute(insert_script_query, val)
                        sqliteConnection.commit()
                        print("MysqlServer Record Updated successfully ")
                        script = ""

                    except:
                        print('error connecting to the server')

        elif re.search(".*(\\\sqlserver)$", subdir) is not None:
            for filename in os.listdir(subdir):
                filepath = os.path.join(subdir, filename)
                print(filepath)

                with open(filepath, 'r') as f:
                    lines = f.readlines()

                    for line in lines:
                        clean_line = line.rstrip()
                        if not clean_line.startswith('-') and not clean_line.startswith('/'):
                            script += clean_line

                    # insert query here
                    try:

                        insert_script_query = """INSERT INTO SqlServer_Scripts(name_version, script) values(?,?);"""
                        val = (version_name, script)
                        cursor.execute(insert_script_query, val)
                        sqliteConnection.commit()
                        print("SqlServer Record Updated successfully ")
                        script = ""

                    except:
                        print('error connecting to the server')