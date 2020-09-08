import os
import re
import sqlite3

import mysql
import pyodbc
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox, QApplication
from dbConnection import db_connection


def show_popup(self, state):
    if state == 'success':
        msg = QMessageBox()
        msg.setWindowTitle("Process Finished !")
        msg.setWindowIcon(QIcon('check.png'))
        msg.setIcon(QMessageBox.Information)
        # msg.setStandardButtons(QMessageBox.Open | QMessageBox.Close)
        # msg.setDefaultButton()
        msg.setText("SUCCESS !!")
        msg.setInformativeText("Process Finished Successfully !!")
        msg.buttonClicked.connect(self.popup_button_clicked)
        msg.exec_()

    elif state == 'server':
        msg = QMessageBox()
        msg.setWindowTitle("Seléctionnez Serveur !")
        msg.setWindowIcon(QIcon('gear.png'))
        msg.setIcon(QMessageBox.Critical)
        # msg.setStandardButtons(QMessageBox.Close)
        # msg.setDefaultButton()
        msg.setText("Vous Devez Seléctionner un serveur !")
        # msg.setInformativeText("Please upload your Excel File !")
        # msg.setDetailedText("Your Reports Are in Reports Folder inder your Desktop")
        # msg.buttonClicked.connect(self.popup_button_clicked)
        msg.exec_()


    elif state == 'fields':
        msg = QMessageBox()
        msg.setWindowTitle("Champs Vides !")
        msg.setWindowIcon(QIcon('gear.png'))
        msg.setIcon(QMessageBox.Critical)
        # msg.setStandardButtons(QMessageBox.Close)
        # msg.setDefaultButton()
        msg.setText("SVP vous de devez remplir les champs nécessaires!")
        # msg.setInformativeText("Please upload your Excel File !")
        # msg.setDetailedText("Your Reports Are in Reports Folder inder your Desktop")
        # msg.buttonClicked.connect(self.popup_button_clicked)
        msg.exec_()

    elif state == 'script_ok':
        msg = QMessageBox()
        msg.setWindowTitle("Succès d'opération !")
        msg.setWindowIcon(QIcon('check.png'))
        msg.setIcon(QMessageBox.Information)
        # msg.setStandardButtons(QMessageBox.Open | QMessageBox.Close)
        # msg.setDefaultButton()
        msg.setText("SUCCES !!")
        msg.setInformativeText("Script importé avec Succès !!")
        msg.buttonClicked.connect(self.popup_button_clicked)
        msg.exec_()

    elif state == 'param_server':
        msg = QMessageBox()
        msg.setWindowTitle("Erreur Serveur  !")
        msg.setWindowIcon(QIcon('gear.png'))
        msg.setIcon(QMessageBox.Critical)
        # msg.setStandardButtons(QMessageBox.Close)
        # msg.setDefaultButton()
        msg.setText("SVP vérifiez votre connection à la base de données!")
        # msg.setInformativeText("Please upload your Excel File !")
        # msg.setDetailedText("Your Reports Are in Reports Folder inder your Desktop")
        # msg.buttonClicked.connect(self.popup_button_clicked)
        msg.exec_()

    elif state == 'end_ok':
        msg = QMessageBox()
        msg.setWindowTitle("Succès d'opération !")
        msg.setWindowIcon(QIcon('check.png'))
        msg.setIcon(QMessageBox.Information)
        # msg.setStandardButtons(QMessageBox.Open | QMessageBox.Close)
        # msg.setDefaultButton()
        msg.setText("SUCCES !!")
        msg.setInformativeText("Script exécuté avec Succès !!")
        # msg.buttonClicked.connect(self.popup_button_clicked)
        msg.exec_()

    elif state == 'end_with_err':
        msg = QMessageBox()
        msg.setWindowTitle("Erreur !")
        msg.setWindowIcon(QIcon('gear.png'))
        msg.setIcon(QMessageBox.Critical)
        # msg.setStandardButtons(QMessageBox.Close)
        # msg.setDefaultButton()
        msg.setText("opération terminée avec erreurs voir Log pour plus de détails !")
        # msg.setInformativeText("Please upload your Excel File !")
        # msg.setDetailedText("Your Reports Are in Reports Folder inder your Desktop")
        # msg.buttonClicked.connect(self.popup_button_clicked)
        msg.exec_()

    elif state == 'db_name':
        msg = QMessageBox()
        msg.setWindowTitle("Warning !")
        msg.setWindowIcon(QIcon('gear.png'))
        msg.setIcon(QMessageBox.Warning)
        # msg.setStandardButtons(QMessageBox.Close)
        # msg.setDefaultButton()
        msg.setText("SVP donnez un nom de base de données  !")
        # msg.setDetailedText("Your Reports Are in Reports Folder inder your Desktop")
        # msg.buttonClicked.connect(self.popup_button_clicked)
        msg.exec_()

    elif state == 'version_name':
        msg = QMessageBox()
        msg.setWindowTitle("Warning !")
        msg.setWindowIcon(QIcon('gear.png'))
        msg.setIcon(QMessageBox.Warning)
        # msg.setStandardButtons(QMessageBox.Close)
        # msg.setDefaultButton()
        msg.setText("SVP Vous devez ajouter un nom de version !")
        # msg.setInformativeText("SVP associez un script à cette version avant de proccéder!")
        # msg.setDetailedText("Your Reports Are in Reports Folder inder your Desktop")
        # msg.buttonClicked.connect(self.popup_button_clicked)
        msg.exec_()

    elif state == 'version_empty':
        msg = QMessageBox()
        msg.setWindowTitle("Warning !")
        msg.setWindowIcon(QIcon('gear.png'))
        msg.setIcon(QMessageBox.Warning)
        # msg.setStandardButtons(QMessageBox.Close)
        # msg.setDefaultButton()
        msg.setText("SVP selectionnez une version ou Importer une si vous n'avez pas encore fait !")
        # msg.setInformativeText("SVP associez un script à cette version avant de proccéder!")
        # msg.setDetailedText("Your Reports Are in Reports Folder inder your Desktop")
        # msg.buttonClicked.connect(self.popup_button_clicked)
        msg.exec_()

    elif state == 'script_creation':
        msg = QMessageBox()
        msg.setWindowTitle("Warning !")
        msg.setWindowIcon(QIcon('gear.png'))
        msg.setIcon(QMessageBox.Warning)
        # msg.setStandardButtons(QMessageBox.Close)
        # msg.setDefaultButton()
        msg.setText("SVP selectionnez un Script de Création !")
        # msg.setInformativeText("SVP associez un script à cette version avant de proccéder!")
        # msg.setDetailedText("Your Reports Are in Reports Folder inder your Desktop")
        # msg.buttonClicked.connect(self.popup_button_clicked)
        msg.exec_()


def admin(err):
    msg = QMessageBox()
    msg.setWindowTitle("Warning !")
    msg.setWindowIcon(QIcon('gear.png'))
    msg.setIcon(QMessageBox.Warning)
    # msg.setStandardButtons(QMessageBox.Close)
    # msg.setDefaultButton()
    msg.setText(err)
    # msg.setInformativeText("SVP associez un script à cette version avant de proccéder!")
    # msg.setDetailedText("Your Reports Are in Reports Folder inder your Desktop")
    # msg.buttonClicked.connect(self.popup_button_clicked)
    msg.exec_()




def end_with_err(log_path):
    msg = QMessageBox()
    msg.setWindowTitle("Erreur !")
    msg.setWindowIcon(QIcon('gear.png'))
    msg.setIcon(QMessageBox.Critical)
    # msg.setStandardButtons(QMessageBox.Close)
    # msg.setDefaultButton()
    msg.setText("opération terminée avec erreurs voir Log pour plus de détails !")
    msg.setInformativeText("Emplacement log: \n" + log_path)
    # msg.setDetailedText("Your Reports Are in Reports Folder inder your Desktop")
    # msg.buttonClicked.connect(self.popup_button_clicked)
    msg.exec_()


def show_popup_script():
    msg = QMessageBox()
    msg.setWindowTitle("Succès d'opération !")
    msg.setWindowIcon(QIcon('check.png'))
    msg.setIcon(QMessageBox.Information)
    # msg.setDefaultButton()
    msg.setText("SUCCES !!")
    msg.setInformativeText("Script importé avec Succès !!")
    # msg.buttonClicked.connect(self.popup_button_clicked)
    msg.exec_()


def import_script_svp():
    msg = QMessageBox()
    msg.setWindowTitle("Seléctionner Script !")
    msg.setWindowIcon(QIcon('gear.png'))
    msg.setIcon(QMessageBox.Critical)
    # msg.setStandardButtons(QMessageBox.Close)
    # msg.setDefaultButton()
    msg.setText("Vous Devez seléctionner une version !")
    # msg.setInformativeText("Please upload your Excel File !")
    # msg.setDetailedText("Your Reports Are in Reports Folder inder your Desktop")
    # msg.buttonClicked.connect(self.popup_button_clicked)
    msg.exec_()


def sqlite_error(error):
    msg = QMessageBox()
    msg.setWindowTitle("Error Connection !")
    msg.setWindowIcon(QIcon('gear.png'))
    msg.setIcon(QMessageBox.Critical)
    # msg.setStandardButtons(QMessageBox.Close)
    # msg.setDefaultButton()
    msg.setText(error)
    # msg.setInformativeText("Please upload your Excel File !")
    # msg.setDetailedText("Your Reports Are in Reports Folder inder your Desktop")
    # msg.buttonClicked.connect(self.popup_button_clicked)
    msg.exec_()


def db_errors(error):
    msg = QMessageBox()
    msg.setWindowTitle("Erreur Connection !")
    msg.setWindowIcon(QIcon('gear.png'))
    msg.setIcon(QMessageBox.Critical)
    # msg.setStandardButtons(QMessageBox.Close)
    # msg.setDefaultButton()
    msg.setText(error)
    # msg.setInformativeText("Please upload your Excel File !")
    # msg.setDetailedText("Your Reports Are in Reports Folder inder your Desktop")
    # msg.buttonClicked.connect(self.popup_button_clicked)
    msg.exec_()


def test_popup():
    msg = QMessageBox()
    msg.setWindowTitle("Erreur Connection !")
    msg.setWindowIcon(QIcon('gear.png'))
    msg.setIcon(QMessageBox.Critical)
    # msg.setStandardButtons(QMessageBox.Close)
    # msg.setDefaultButton()
    msg.setText('test popup work')
    # msg.setInformativeText("Please upload your Excel File !")
    # msg.setDetailedText("Your Reports Are in Reports Folder inder your Desktop")
    # msg.buttonClicked.connect(self.popup_button_clicked)
    msg.exec_()


def debut_fin(err):
    msg = QMessageBox()
    msg.setWindowTitle("Warning !")
    msg.setWindowIcon(QIcon('gear.png'))
    msg.setIcon(QMessageBox.Warning)
    # msg.setStandardButtons(QMessageBox.Close)
    # msg.setDefaultButton()
    msg.setText(err)
    # msg.setInformativeText("SVP associez un script à cette version avant de proccéder!")
    # msg.setDetailedText("Your Reports Are in Reports Folder inder your Desktop")
    # msg.buttonClicked.connect(self.popup_button_clicked)
    msg.exec_()


def validate_ip(ip):
    pass


def createDirectory(path):
    if not os.path.exists(os.path.expandvars(path)):
        os.makedirs(os.path.expandvars(path))


def save_connection(db_type, host, port, user, password, dbname):
    sqliteConnection, cursor = db_connection()
    save_connection = False

    if db_type == "MySQL":

        try:

            sql_update_query = """Update parametrage_serveur set host = ?, port = ?, user = ?, password = ?, dbName = ? where type = ?"""
            val = (host, port, user, password, dbname, db_type)
            cursor.execute(sql_update_query, val)
            sqliteConnection.commit()
            print("Mysql Record Updated successfully ")
            cursor.close()
            if (sqliteConnection):
                sqliteConnection.close()
            save_connection = True
            return save_connection

        except:
            admin('SVP Lancer l\'application En tant qu\'Administrateur '
                  'pour que vous puissiez soumettre vos changement à la base de donnée !')
            return save_connection


    else:

        try:
            sql_update_query = """Update parametrage_serveur set host = ?, port = ?, user = ?, password = ?, dbName = ? where type = ?"""
            val = (host, port, user, password, dbname, db_type)
            cursor.execute(sql_update_query, val)
            sqliteConnection.commit()
            print("SQL server Record Updated successfully ")
            cursor.close()
            if (sqliteConnection):
                sqliteConnection.close()
            save_connection = True
            return save_connection

        except:
            admin('SVP Lancer l\'application En tant qu\'Administrateur '
                  'pour que vous puissiez soumettre vos changement à la base de donnée !')
            return save_connection


def list_version(server):
    sqliteConnection, cursor = db_connection()

    try:
        if server == "MySQL":
            list_version = """select DISTINCT name_version from {}""".format('Mysql_Scripts')
            list_version = cursor.execute(list_version)
            return list_version
        else:
            list_version = """select DISTINCT  name_version from {}""".format('SqlServer_Scripts')
            list_version = cursor.execute(list_version)
            return list_version
    except sqlite3.Error as e:
        print(e)


def save_scripts(path):
    script_saved = False
    script = ""
    jackpot_regex = r"(^\s*\*)|(^\s*/)|(^\s*-)|(^\s*\*)"
    sqliteConnection, cursor = db_connection()
    version_names_list = os.listdir(path)
    for version_name in version_names_list:
        version_dir_path = os.path.join(path, version_name)

        for subdir, dirs, files in os.walk(version_dir_path):

            if re.search(".*(\\\mysql)$", subdir) is not None:

                for filename in os.listdir(subdir):
                    filepath = os.path.join(subdir, filename)

                    with open(filepath, 'r',errors='ignore') as f:
                        lines = f.readlines()

                        for line in lines:
                            clean_line = line.rstrip()

                            if not re.match(jackpot_regex, clean_line):
                                # if not clean_line.startswith('-') and not clean_line.startswith(
                                #         '/') and not clean_line.startswith(' *'):
                                script += clean_line

                        # insert query here
                        try:

                            insert_script_query = """INSERT INTO Mysql_Scripts(name_version, script) values(?,?);"""
                            val = (version_name, script)
                            cursor.execute(insert_script_query, val)
                            sqliteConnection.commit()
                            print("MysqlServer Record Updated successfully ")
                            script = ""
                            script_saved = True

                        except sqlite3.Error as err:
                            print(err)

            elif re.search(".*(\\\sqlserver)$", subdir) is not None:
                for filename in os.listdir(subdir):
                    filepath = os.path.join(subdir, filename)

                    with open(filepath, 'r',errors='ignore') as f:
                        lines = f.readlines()

                        for line in lines:
                            clean_line = line.rstrip()
                            if not re.match(jackpot_regex, clean_line):
                                # if not clean_line.startswith('-') and not clean_line.startswith(
                                #         '/') and not clean_line.startswith(' *'):
                                script += clean_line

                        # insert query here
                        try:

                            insert_script_query = """INSERT INTO SqlServer_Scripts(name_version, script) values(?,?);"""
                            val = (version_name, script)
                            cursor.execute(insert_script_query, val)
                            sqliteConnection.commit()
                            print("SqlServer Record Updated successfully")
                            script = ""
                            script_saved = True

                        except sqlite3.Error as err:
                            print(err)

    return script_saved


def execute_script(self, server, version_debut, version_fin, server_connection, server_cursor, sqlite_cursor):

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
