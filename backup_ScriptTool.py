# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ScriptTool_1.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING! All changes made in this file will be lost!
import os
import re
import sqlite3
from datetime import datetime

import mysql
import pyodbc
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import qApp, QApplication

import functions as my_fnc
from about_big import Ui_About
from ajouter_version import Ui_Version
from import_script import Ui_import_script
from mysql_form import Ui_Mysql
from sqlserver_form import Ui_SQLServer
import dbConnection as conn
from mysql.connector import Error


class Ui_MainWindow(object):
    select_server_val = ""
    select_version_val = ""
    select_version_debut_val = ""
    select_version_fin_val = ""
    select_server_creation_val = ""
    host = ""
    port = ""
    user = ""
    password = ""
    dbname = ""
    nb_query = 0

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowIcon(QIcon('iconBig.gif'))
        # MainWindow.resize(800, 600)
        MainWindow.setFixedSize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(9, 9, 249, 93))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.demarrer_btn = QtWidgets.QPushButton(self.centralwidget)
        self.demarrer_btn.setGeometry(QtCore.QRect(350, 290, 121, 37))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.demarrer_btn.sizePolicy().hasHeightForWidth())
        self.demarrer_btn.setSizePolicy(sizePolicy)
        self.demarrer_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.demarrer_btn.setStyleSheet("QPushButton:hover:!pressed\n"
                                        "{\n"
                                        "  border: 1px solid lime;\n"
                                        "background-color: rgb(0, 0, 0);\n"
                                        "font: 75 16pt \"Cambria\";\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton\n"
                                        "{\n"
                                        "background-color: rgb(0, 0, 0);\n"
                                        "font: 75 16pt \"Cambria\";\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "padding:5px;\n"
                                        "}\n"
                                        "\n"
                                        "\n"
                                        "\n"
                                        "")
        self.demarrer_btn.setObjectName("demarrer_btn")
        self.log_group = QtWidgets.QGroupBox(self.centralwidget)
        self.log_group.setGeometry(QtCore.QRect(30, 334, 741, 201))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.log_group.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.log_group.setFont(font)
        self.log_group.setObjectName("log_group")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.log_group)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.log_area = QtWidgets.QPlainTextEdit(self.log_group)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.log_area.setFont(font)
        self.log_area.setReadOnly(True)
        self.log_area.setObjectName("log_area")
        self.verticalLayout_7.addWidget(self.log_area)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(250, 50, 301, 141))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.param_group = QtWidgets.QGroupBox(self.centralwidget)
        self.param_group.setGeometry(QtCore.QRect(30, 40, 741, 231))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.param_group.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.param_group.setFont(font)
        self.param_group.setObjectName("param_group")
        self.groupBox = QtWidgets.QGroupBox(self.param_group)
        self.groupBox.setGeometry(QtCore.QRect(40, 60, 291, 161))
        self.groupBox.setStyleSheet("QGroupBox {color: white;}")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 40, 81, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.select_version_debut = QtWidgets.QComboBox(self.groupBox)
        self.select_version_debut.setGeometry(QtCore.QRect(120, 40, 161, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.select_version_debut.setFont(font)
        self.select_version_debut.setObjectName("select_version_debut")
        self.select_version_debut.addItem("")
        self.select_version_fin = QtWidgets.QComboBox(self.groupBox)
        self.select_version_fin.setGeometry(QtCore.QRect(120, 80, 161, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.select_version_fin.setFont(font)
        self.select_version_fin.setObjectName("select_version_fin")
        self.select_version_fin.addItem("")
        self.select_server = QtWidgets.QComboBox(self.groupBox)
        self.select_server.setGeometry(QtCore.QRect(120, 120, 161, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.select_server.setFont(font)
        self.select_server.setObjectName("select_server")
        self.select_server.addItem("")
        self.select_server.addItem("")
        # self.select_server.addItem("")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 71, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_3.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 120, 71, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.param_group)
        self.groupBox_2.setGeometry(QtCore.QRect(340, 60, 391, 161))
        self.groupBox_2.setStyleSheet("QGroupBox {color: white;}")
        self.groupBox_2.setObjectName("groupBox_2")
        self.creation_script = QtWidgets.QPushButton(self.groupBox_2)
        self.creation_script.setGeometry(QtCore.QRect(20, 80, 75, 23))
        self.creation_script.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.creation_script.setObjectName("creation_script")
        self.creation_script.setStyleSheet(
            """QPushButton:hover:!pressed{border: 1px solid lime;background-color:black;color:white;}""")
        self.creation_edit = QtWidgets.QLineEdit(self.groupBox_2)
        self.creation_edit.setGeometry(QtCore.QRect(110, 80, 271, 21))
        self.creation_edit.setObjectName("creation_edit")
        self.select_server_creation = QtWidgets.QComboBox(self.groupBox_2)
        self.select_server_creation.setGeometry(QtCore.QRect(110, 40, 131, 22))
        self.select_server_creation.setObjectName("select_server_creation")
        self.select_server_creation.addItem("")
        self.select_server_creation.addItem("")
        self.server_creation_label = QtWidgets.QLabel(self.groupBox_2)
        self.server_creation_label.setGeometry(QtCore.QRect(20, 40, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.server_creation_label.setFont(font)
        self.server_creation_label.setStyleSheet("QLabel{color:white}")
        self.server_creation_label.setObjectName("server_creation_label")
        self.mis_a_jour = QtWidgets.QRadioButton(self.param_group)
        self.mis_a_jour.setGeometry(QtCore.QRect(40, 30, 82, 17))
        self.mis_a_jour.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mis_a_jour.setObjectName("mis_a_jour")
        self.creation = QtWidgets.QRadioButton(self.param_group)
        self.creation.setGeometry(QtCore.QRect(340, 30, 82, 17))
        self.creation.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.creation.setObjectName("creation")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuparametres = QtWidgets.QMenu(self.menubar)
        self.menuparametres.setObjectName("menuparametres")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.statusbar.setStyleSheet("""QStatusBar{background-color:black;color:white;}""")
        MainWindow.setStatusBar(self.statusbar)
        self.actionMysql = QtWidgets.QAction(MainWindow)
        self.actionMysql.setObjectName("actionMysql")
        self.actionSqlServer = QtWidgets.QAction(MainWindow)
        self.actionSqlServer.setObjectName("actionSqlServer")
        self.actionMysql_2 = QtWidgets.QAction(MainWindow)
        self.actionMysql_2.setObjectName("actionMysql_2")
        self.actionSQL_Server = QtWidgets.QAction(MainWindow)
        self.actionSQL_Server.setObjectName("actionSQL_Server")
        self.actionMysql_3 = QtWidgets.QAction(MainWindow)
        self.actionMysql_3.setObjectName("actionMysql_3")
        self.actionSQL_Server_2 = QtWidgets.QAction(MainWindow)
        self.actionSQL_Server_2.setObjectName("actionSQL_Server_2")

        # Ajouter Version
        # self.actionAddversion = QtWidgets.QAction(MainWindow)
        # self.actionAddversion.setObjectName("actionAddversion")
        # self.actionAddversion.setIcon(QIcon('add.png'))

        # Import Script
        self.actionImportscript = QtWidgets.QAction(MainWindow)
        self.actionImportscript.setObjectName("actionImportscript")
        self.actionImportscript.setIcon(QIcon('Upload_16x16.png'))

        # Exit
        self.actionexit = QtWidgets.QAction(MainWindow)
        self.actionexit.setObjectName("actionexit")
        self.actionexit.setIcon(QIcon('Log Out_16x16.png'))
        # About
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAbout.setIcon(QIcon('Information_16x16.png'))

        self.menuparametres.addAction(self.actionMysql_3)
        self.menuparametres.addSeparator()
        self.menuparametres.addAction(self.actionSQL_Server_2)
        self.menuparametres.addSeparator()
        # self.menuparametres.addAction(self.actionAddversion)
        # self.menuparametres.addSeparator()
        self.menuparametres.addAction(self.actionImportscript)
        self.menuparametres.addSeparator()
        self.menuparametres.addAction(self.actionAbout)
        self.menuparametres.addSeparator()
        self.menuparametres.addAction(self.actionexit)
        self.menubar.addAction(self.menuparametres.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        """ my changes in view"""
        # hide group
        # self.log_group.hide()
        self.mis_a_jour.setChecked(True)
        self.creation_script.setEnabled(False)
        self.creation_edit.setEnabled(False)
        self.select_server_creation.setEnabled(False)

        self.actionMysql_3.setIcon(QIcon('mysql.png'))
        self.actionSQL_Server_2.setIcon(QIcon('sql-server-icon-png-11347.png'))
        self.demarrer_btn.setIcon(QIcon('gear.png'))
        self.demarrer_btn.setIconSize(QSize(25, 25))
        # self.menuparametres.setIcon(QIcon('./Icons/Settings_32x32.png'))
        # self.menuparametres.setIconSize(QSize(32, 32))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Scripts Tool V1.0.0"))
        self.demarrer_btn.setText(_translate("MainWindow", "Démarrer"))
        self.log_group.setTitle(_translate("MainWindow", "Log Details:"))
        self.param_group.setTitle(_translate("MainWindow", "Opérations:"))
        self.groupBox.setTitle(_translate("MainWindow", "Mise à jour:"))
        self.label.setText(_translate("MainWindow", "Version début:"))
        self.select_version_debut.setItemText(0, _translate("MainWindow", "Select Version ..."))
        self.select_version_fin.setItemText(0, _translate("MainWindow", "Select Version ..."))

        self.select_server.setItemText(0, _translate("MainWindow", "MySQL"))
        self.select_server.setItemText(1, _translate("MainWindow", "SQL Server"))
        self.label_3.setText(_translate("MainWindow", "Version Fin:"))
        self.label_2.setText(_translate("MainWindow", "Serveur:"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Création:"))
        self.creation_script.setText(_translate("MainWindow", "Parcourir ..."))
        self.select_server_creation.setItemText(0, _translate("MainWindow", "MySQL"))
        self.select_server_creation.setItemText(1, _translate("MainWindow", "SQL Server"))
        self.server_creation_label.setText(_translate("MainWindow", "Serveur:"))
        self.mis_a_jour.setText(_translate("MainWindow", "Mise à jour"))
        self.creation.setText(_translate("MainWindow", "Création"))
        self.menuparametres.setTitle(_translate("MainWindow", "Paramétrage"))
        self.actionMysql.setText(_translate("MainWindow", "Mysql"))
        self.actionSqlServer.setText(_translate("MainWindow", "SqlServer"))
        self.actionMysql_2.setText(_translate("MainWindow", "Mysql"))
        self.actionSQL_Server.setText(_translate("MainWindow", "SQL Server"))
        self.actionMysql_3.setText(_translate("MainWindow", "Mysql"))
        self.actionSQL_Server_2.setText(_translate("MainWindow", "SQL Server"))
        # self.actionAddversion.setText(_translate("MainWindow", "Ajouter Version"))
        self.actionImportscript.setText(_translate("MainWindow", "Importer Version"))
        self.actionexit.setText(_translate("MainWindow", "Exit"))
        self.actionAbout.setText(_translate("MainWindow", "à propos"))
        self.actionexit.setShortcut(_translate("MainWindow", "Ctrl+Q"))

        # Set Action Quit Application
        self.actionexit.setStatusTip(_translate("MainWindows", 'Exit application !'))
        self.actionexit.triggered.connect(qApp.quit)
        self.actionAbout.triggered.connect(self.open_about)

        # ToolTips
        # self.actionAddversion.setStatusTip(_translate("MainWindows", 'Ajouter Version !'))
        self.actionImportscript.setStatusTip(_translate("MainWindows", 'Importer Version !'))
        self.actionAbout.setStatusTip(_translate("MainWindows", 'à propos de l\'application !'))
        self.actionSQL_Server_2.setStatusTip(_translate("MainWindows", 'Paramétrage serveur SQL Server !'))
        self.actionMysql_3.setStatusTip(_translate("MainWindows", 'Paramétrage serveur Mysql !'))

        """ This is my logic """
        self.populate_version()
        # self.select_version_val = str(self.select_version_debut.currentText())
        self.select_version_debut_val = str(self.select_version_debut.currentText())
        self.select_version_fin_val = str(self.select_version_fin.currentText())
        self.select_server_creation_val = str(self.select_server_creation.currentText())
        self.select_server_val = str(self.select_server.currentText())
        self.actionMysql_3.triggered.connect(self.open_mysql_param)
        self.actionSQL_Server_2.triggered.connect(self.open_sqlserver_param)
        self.actionImportscript.triggered.connect(self.open_import_script)
        # self.actionAddversion.triggered.connect(self.open_ajouter_version)
        self.demarrer_btn.clicked.connect(self.run_script)
        self.creation_script.clicked.connect(self.upload_file)

        self.select_server.currentTextChanged.connect(self.get_server)
        self.select_version_debut.currentTextChanged.connect(self.get_version_debut)
        self.select_version_fin.currentTextChanged.connect(self.get_version_fin)
        self.select_server_creation.currentTextChanged.connect(self.get_server_creation)
        self.mis_a_jour.toggled.connect(lambda: self.radiostate(self.mis_a_jour))
        self.creation.toggled.connect(lambda: self.radiostate(self.creation))

    def run_script(self):
        jackpot_regex = r"(^\s*\*)|(^\s*/)|(^\s*-)|(^\s*\*)"
        query = ""
        nb_query_executed = 0
        nb_query_failed = 0
        dir_path = r'C:\users\%username%\Desktop\ScriptTool_Log'
        timestump = datetime.today().strftime('%Y-%m-%d-%H_%M_%S')
        errors = ""
        creation_errors = False

        if self.mis_a_jour.isChecked():

            self.log_area.clear()

            version_debut = self.select_version_debut_val
            version_fin = self.select_version_fin_val
            server = self.select_server_val
            # dir_path = r'C:\users\%username%\Desktop\ScriptTool_Log'
            # timestump = datetime.today().strftime('%Y-%m-%d-%H_%M_%S')

            sqliteConnection, cursor = conn.db_connection()
            try:
                sql_select_query = """select host,port,user,password,dbName from parametrage_serveur where type=?"""
                val = (self.select_server_val,)
                col = cursor.execute(sql_select_query, val)

                for i in col:
                    self.host = i[0]
                    self.port = i[1]
                    self.user = i[2]
                    self.password = i[3]
                    self.dbname = i[4]

            except sqlite3.Error as e:

                my_fnc.db_errors(str(e))

            if self.host == "" and self.port == "" and self.user == "" and self.password == "" and self.dbname == "":
                # print('popup SVP parameter sever first')
                my_fnc.show_popup(self, 'param_server')

            else:

                server_connection, server_cursor = conn.db_connection_server(self.select_server_val,
                                                                             self.host,
                                                                             self.port,
                                                                             self.user, self.password,
                                                                             self.dbname)
                if str(server_connection) != 'None':

                    if version_debut != "" and version_fin != "":

                        end_with_err, errors, queries_executed, nb_query_executed, nb_query_failed, server_type = my_fnc.execute_script(
                            self, server, version_debut, version_fin,
                            server_connection,
                            server_cursor, cursor)

                        if end_with_err and queries_executed != "":
                            # put errors in log file
                            my_fnc.createDirectory(os.path.join(dir_path, server_type))
                            with open(
                                    os.path.expandvars(
                                        os.path.join(dir_path, server_type)) + r'\Log_' + timestump + '.log',
                                    'w') as log_file:
                                log_file.write(str(errors))

                            # self.log_area.setPlainText('Requêtes Exécutées avec Succès:\n\n' + str(queries_executed))
                            # self.log_area.setStyleSheet("QPlainTextEdit{color:green}")

                            # self.log_area.setPlainText('Résumé de l\'opération:\n\n' + 'Nombre de Requêtes éxecutées Avec Succès: '+str(nb_query_executed)+'\n'+
                            #                            'Nombre de Requêtes échouées: '+str(nb_query_failed))
                            self.log_area.clear()
                            self.log_area.appendHtml(
                                '<html><p>Résumé de l\'opération:</p><p style="color:green;">Nombre de Requêtes éxecutées Avec Succès: ' + str(
                                    nb_query_executed) + '</p></br><p style="color:red;">Nombre de Requêtes échouées: ' + str(
                                    nb_query_failed) + '</p></html>')
                            # self.log_area.setStyleSheet("QPlainTextEdit{color:green}")
                            my_fnc.end_with_err(os.path.expandvars(dir_path))

                            # my_fnc.show_popup(self, 'end_with_err')

                        elif end_with_err:
                            # put errors in log file
                            my_fnc.createDirectory(os.path.join(dir_path, server_type))
                            with open(
                                    os.path.expandvars(
                                        os.path.join(dir_path, server_type)) + r'\Log_' + timestump + '.log',
                                    'w') as log_file:
                                log_file.write(str(errors))

                            self.log_area.setPlainText(
                                'Résumé de l\'opération:\n' +
                                'Nombre de Requêtes échouées: ' + str(nb_query_failed))

                            my_fnc.end_with_err(os.path.expandvars(dir_path))

                        elif queries_executed != "" and not end_with_err:
                            self.log_area.setPlainText(
                                'Résumé de l\'opération:\n' + 'Nombre de Requêtes éxecutées Avec Succès: ' + str(
                                    nb_query_executed))

                            my_fnc.show_popup(self, 'end_ok')

                    else:
                        my_fnc.show_popup(self, 'version_empty')

                else:
                    print('server connection error !')
        else:

            """ Add creation logic here """
            if self.select_server_creation_val == "MySQL":
                except_to_use = mysql.connector.Error

            else:
                except_to_use = pyodbc.Error
            sqliteConnection, cursor = conn.db_connection()

            try:
                sql_select_query = """select host,port,user,password,dbName from parametrage_serveur where type=?"""
                val = (self.select_server_creation_val,)
                col = cursor.execute(sql_select_query, val)

                for i in col:
                    self.host = i[0]
                    self.port = i[1]
                    self.user = i[2]
                    self.password = i[3]
                    self.dbname = i[4]

            except sqlite3.Error as e:

                my_fnc.db_errors(str(e))

            if self.host == "" and self.port == "" and self.user == "" and self.password == "" and self.dbname == "":
                # print('popup SVP parameter sever first')
                my_fnc.show_popup(self, 'param_server')

            else:

                server_connection, server_cursor = conn.db_connection_server(self.select_server_val,
                                                                             self.host,
                                                                             self.port,
                                                                             self.user, self.password,
                                                                             self.dbname)

                if self.creation_edit.text() != "":

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
                    my_fnc.show_popup(self, 'script_creation')


    def get_server(self):
        self.select_server_val = str(self.select_server.currentText())
        self.populate_version()

    def get_version_debut(self):
        self.select_version_debut_val = str(self.select_version_debut.currentText())

    def get_server_creation(self):
        self.select_server_creation_val = str(self.select_server_creation.currentText())

    def get_version_fin(self):

        self.select_version_fin_val = str(self.select_version_fin.currentText())
        # self.select_version_val = str(self.select_version_fin.currentText())

    def populate_version(self):

        self.select_version_debut.clear()
        self.select_version_fin.clear()
        list_version = my_fnc.list_version(str(self.select_server.currentText()))

        for i in list_version:
            self.select_version_debut.addItem(str(i[0]))
            self.select_version_fin.addItem(str(i[0]))

    def open_mysql_param(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Mysql()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_sqlserver_param(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_SQLServer()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_about(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_About()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_import_script(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_import_script()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_ajouter_version(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Version()
        self.ui.setupUi(self.window)
        self.window.show()

    def radiostate(self, b):

        if b.isChecked() and b.text() == "Mise à jour":
            self.creation_script.setEnabled(False)
            self.select_server_creation.setEnabled(False)
            self.creation_edit.clear()
            self.select_version_debut.setEnabled(True)
            self.select_version_fin.setEnabled(True)
            self.select_server.setEnabled(True)
        else:
            self.creation_script.setEnabled(True)
            self.select_server_creation.setEnabled(True)
            self.select_version_debut.setEnabled(False)
            self.select_version_fin.setEnabled(False)
            self.select_server.setEnabled(False)

    def upload_file(self):

        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        self.file_path, _ = QtWidgets.QFileDialog.getOpenFileName(
            None,
            "Open File",
            "",
            "SQL Files (*.sql)",
            options=options)
        self.creation_edit.setText(self.file_path)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
