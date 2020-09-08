def execute_script(server, version_debut, version_fin, server_connection, server_cursor, sqlite_cursor):

    nb_query_executed = 0
    nb_query_failed=0
    # nb_query_to_execute = 0
    errors = ""
    queries_executed = ""
    end_with_err = False


    try:
        # query id_script of Versions
        id_debut_query = """SELECT id_script FROM Mysql_Scripts WHERE name_version='{}'""".format(version_debut)
        id_fin_query = """SELECT id_script FROM Mysql_Scripts WHERE name_version='{}'""".format(version_fin)

        sqlite_cursor.execute(id_debut_query)
        id_debut_result = sqlite_cursor.fetchone()

        sqlite_cursor.execute(id_fin_query)
        id_fin_result = sqlite_cursor.fetchall()

        id_debut = id_debut_result[0]
        id_fin = id_fin_result[-1][-1]

        if id_debut > id_fin:
            debut_fin('SVP la version début doit être infériere à celle de la fin !')
            return end_with_err, errors, queries_executed, nb_query_executed, nb_query_failed, server
        else:

            """logic of executing the script goes here"""
            if server == "MySQL":

                if str(server_connection) != "None" and str(server_cursor) != "None":

                    try:

                        sql_select_query = """
                               SELECT * 
                               FROM Mysql_Scripts 
                               WHERE id_script BETWEEN {} and {} """.format(id_debut,
                                                                            id_fin)

                        sqlite_cursor.execute(sql_select_query)
                        scripts = sqlite_cursor.fetchall()
                        for script in scripts:

                            script_to_execute = filter(None, str(script[2]).split(';'))
                            id_script = str(script[0])
                            name_version = str(script[1])

                            # calculate nbr_query here for the progressBar
                            # for b in script_to_execute:
                            #     nb_query_to_execute += 1
                            # print('this is the nbr_query to execute:', nb_query_to_execute)

                            for i in script_to_execute:
                                # strip() removes leading and trailing white spaces
                                # semicolon is re-added per line for query run
                                query = i.strip() + ';'

                                try:

                                    server_cursor.execute(query)
                                    server_connection.commit()
                                    print("Script inserted successfully ")
                                    QApplication.processEvents()
                                    self.log_area.setPlainText(str(query))
                                    queries_executed += str(query) + '\n\n'
                                    nb_query_executed+=1


                                except mysql.connector.Error as err:

                                    errors += str(
                                        err) + 'le Script Numéro:  ' + id_script + '  de la version:  ' + name_version + ' ->' + str(
                                        query) + '\n\n'
                                    end_with_err = True
                                    nb_query_failed+=1

                        return end_with_err, errors, queries_executed, nb_query_executed, nb_query_failed, server


                    except sqlite3.Error as e:
                        print(e)
                else:
                    return end_with_err, errors, queries_executed, nb_query_executed, nb_query_failed, server
                    print('server Error')

            # if of SQLServeur
            else:

                try:
                    sql_select_query = """
                                      SELECT script 
                                      FROM SqlServer_Scripts 
                                      WHERE id_script BETWEEN {} and {} """.format(id_debut,
                                                                                   id_fin)
                    sqlite_cursor.execute(sql_select_query)
                    scripts = sqlite_cursor.fetchall()
                    for script in scripts:

                        script_to_execute = filter(None, str(script[0]).split(';'))
                        id_script = str(script[0])
                        name_version = str(script[1])

                        for i in script_to_execute:
                            # strip() removes leading and trailing white spaces
                            # semicolon is re-added per line for query run
                            query = i.strip() + ';'

                            try:

                                server_cursor.execute(query)
                                server_connection.commit()
                                print("Script inserted successfully ")
                                QApplication.processEvents()
                                self.log_area.setPlainText(str(query))
                                queries_executed += str(query) + '\n\n'
                                nb_query_executed += 1


                            except pyodbc.Error as err:
                                errors += str(
                                    err) + 'le Script Numéro:  ' + id_script + '  de la version:  ' + name_version + ' ->' + str(
                                    query) + '\n\n'
                                end_with_err = True
                                nb_query_failed += 1

                    return end_with_err, errors, queries_executed, nb_query_executed, nb_query_failed, server


                except sqlite3.Error as e:
                    print(e)


    except sqlite3.Error as err:
        db_errors(err)
