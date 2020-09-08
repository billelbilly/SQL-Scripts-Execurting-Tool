import re

jackpot_regex = r"(^\s*\*)|(^\s*/)|(^\s*-)|(^\s*\*)"
query = ""
nb_query_executed = 0
nb_query_failed = 0
dir_path = r'C:\users\%username%\Desktop\ScriptTool_Log'
timestump = datetime.today().strftime('%Y-%m-%d-%H_%M_%S')
errors = ""
creation_errors = False

server_connection, server_cursor = conn.db_connection_server(self.select_server_creation_val,
                                                             self.host,
                                                             self.port,
                                                             self.user, self.password,
                                                             self.dbname)

if self.creation_edit.text() != "":

    if self.db_name_edit.text() != "":
        create_db_query = "CREATE DATABASE IF NOT EXISTS {};".format(self.db_name_edit.text())
        server_cursor.execute(create_db_query)
        server_connection.commit()
        print('db created successfully')
        self.log_area.setPlainText(str(create_db_query))
        nb_query_executed += 1

        use_db_query = "USE {};".format(self.db_name_edit.text())
        server_cursor.execute(use_db_query)
        server_connection.commit()
        print('db selected successfully ')
        self.log_area.setPlainText(str(use_db_query))
        nb_query_executed += 1

    with open(self.creation_edit.text(), 'r', errors='ignore') as f:

        lines = f.readlines()

        for line in lines:
            clean_line = line.rstrip()
            if not re.match(jackpot_regex, clean_line):
                query += clean_line
                if clean_line.endswith(';'):

                    try:
                        server_cursor.execute(query)
                        server_connection.commit()
                        print("Script inserted successfully ")
                        QApplication.processEvents()
                        self.log_area.setPlainText(str(query))
                        nb_query_executed += 1
                        query = ""


                    except except_to_use as err:
                        errors += str(err) + '\n'
                        nb_query_failed += 1
                        creation_errors = True
                        query = ""

        if creation_errors:
            my_fnc.createDirectory(os.path.join(dir_path, self.select_server_creation_val))
            with open(
                    os.path.expandvars(
                        os.path.join(dir_path,
                                     self.select_server_creation_val)) + r'\Log_' + timestump + '.log',
                    'w') as log_file:
                log_file.write(errors)
                self.log_area.clear()
            my_fnc.end_with_err(os.path.expandvars(dir_path))

        self.log_area.appendHtml(
            '<html><p>Résumé de l\'opération:</p><p style="color:green;">Nombre de Requêtes éxecutées Avec Succès: ' + str(
                nb_query_executed) + '</p></br><p style="color:red;">Nombre de Requêtes échouées: ' + str(
                nb_query_failed) + '</p></html>')


else:
    print("Please select script to execute")
