# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mysql_form.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
import dbConnection as conn
import functions as my_fnc


class Ui_SQLServer(object):
    def setupUi(self, Mysql):
        Mysql.setObjectName("Mysql")
        # Mysql.resize(419, 358)
        Mysql.setFixedSize(419, 358)
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
        Mysql.setPalette(palette)
        self.verticalLayout = QtWidgets.QVBoxLayout(Mysql)
        self.verticalLayout.setObjectName("verticalLayout")
        self.param_serveur = QtWidgets.QGroupBox(Mysql)
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
        self.param_serveur.setPalette(palette)
        self.param_serveur.setObjectName("param_serveur")
        self.host_label = QtWidgets.QLabel(self.param_serveur)
        self.host_label.setGeometry(QtCore.QRect(20, 50, 47, 13))
        self.host_label.setObjectName("host_label")
        self.port_label = QtWidgets.QLabel(self.param_serveur)
        self.port_label.setGeometry(QtCore.QRect(20, 100, 47, 13))
        self.port_label.setObjectName("port_label")
        self.user_label = QtWidgets.QLabel(self.param_serveur)
        self.user_label.setGeometry(QtCore.QRect(20, 150, 47, 13))
        self.user_label.setObjectName("user_label")
        self.pass_label = QtWidgets.QLabel(self.param_serveur)
        self.pass_label.setGeometry(QtCore.QRect(20, 200, 60, 16))
        self.pass_label.setObjectName("pass_label")
        self.host_edit = QtWidgets.QLineEdit(self.param_serveur)
        self.host_edit.setGeometry(QtCore.QRect(110, 40, 201, 31))
        self.host_edit.setObjectName("host_edit")
        self.user_edit = QtWidgets.QLineEdit(self.param_serveur)
        self.user_edit.setGeometry(QtCore.QRect(110, 140, 201, 31))
        self.user_edit.setObjectName("user_edit")
        self.pass_edit = QtWidgets.QLineEdit(self.param_serveur)
        self.pass_edit.setGeometry(QtCore.QRect(110, 190, 201, 31))
        self.pass_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pass_edit.setObjectName("pass_edit")
        self.save_btn = QtWidgets.QPushButton(self.param_serveur)
        self.save_btn.setGeometry(QtCore.QRect(160, 290, 120, 30))
        self.save_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.save_btn.setStyleSheet("QPushButton:hover:!pressed\n"
                                    "{\n"
                                    "  border: 1px solid lime;\n"
                                    "background-color: rgb(0, 0, 0);\n"
                                    "font: 30 12pt \"Cambria\";\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton\n"
                                    "{\n"
                                    "background-color: rgb(0, 0, 0);\n"
                                    "font: 30 12pt \"Cambria\";\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "padding:2px;\n"
                                    "}\n"
                                    "")
        self.save_btn.setObjectName("save_btn")
        self.db_label = QtWidgets.QLabel(self.param_serveur)
        self.db_label.setGeometry(QtCore.QRect(20, 250, 51, 16))
        self.db_label.setObjectName("db_label")
        self.db_edit = QtWidgets.QLineEdit(self.param_serveur)
        self.db_edit.setGeometry(QtCore.QRect(110, 240, 201, 31))
        self.db_edit.setObjectName("db_edit")
        self.port_nbr = QtWidgets.QSpinBox(self.param_serveur)
        self.port_nbr.setGeometry(QtCore.QRect(110, 90, 71, 31))
        self.port_nbr.setMaximum(65535)
        self.port_nbr.setObjectName("port_nbr")
        self.verticalLayout.addWidget(self.param_serveur)

        self.retranslateUi(Mysql)
        QtCore.QMetaObject.connectSlotsByName(Mysql)

        """ my changes in view"""
        self.save_btn.setIcon(QIcon('Save_16x16.png'))
        self.save_btn.setIconSize(QSize(16, 16))

        sqliteConnection, cursor = conn.db_connection()
        try:
            sql_select_query = """select host,port,user,password,dbName from parametrage_serveur where type='SQL Server'"""
            col = cursor.execute(sql_select_query)

            for i in col:
                self.host = i[0]
                self.port = i[1]
                self.user = i[2]
                self.password = i[3]
                self.dbname = i[4]

            self.host_edit.setText(str(self.host))
            if self.port == "":
                self.port_nbr.setValue(0)
            else:
                self.port_nbr.setValue(int(self.port))
            self.user_edit.setText(str(self.user))
            self.pass_edit.setText(str(self.password))
            self.db_edit.setText(str(self.dbname))

        except sqlite3.Error as error:

            print("Error while connecting to sqlite", error)

    def retranslateUi(self, Mysql):
        _translate = QtCore.QCoreApplication.translate
        Mysql.setWindowTitle(_translate("Mysql", "Scripts Tool V1.0.1"))
        self.param_serveur.setTitle(_translate("Mysql", "Paramètres Serveur"))
        self.host_label.setText(_translate("Mysql", "Host:*"))
        self.port_label.setText(_translate("Mysql", "Port:*"))
        self.user_label.setText(_translate("Mysql", "User:*"))
        self.pass_label.setText(_translate("Mysql", "Password:*"))
        self.save_btn.setText(_translate("Mysql", "Enregistrer"))
        self.db_label.setText(_translate("Mysql", "Database:"))
        Mysql.setWindowIcon(QIcon('iconBig.gif'))

        """ This is my logic """
        self.save_btn.clicked.connect(self.save_to_db)

    def save_to_db(self):
        conn.db_connection('sqlserver')

    def save_to_db(self):
        """ Validate Input Fields"""
        if self.host_edit.text() != "" and self.port_nbr.value() != 0 and self.user_edit.text() != "" and self.pass_edit.text() != "":
            """ Save to db """
            save_connection_ok = my_fnc.save_connection(
                'sqlserver',
                self.host_edit.text(),
                self.port_nbr.value(),
                self.user_edit.text(),
                self.pass_edit.text(),
                self.db_edit.text()
            )

            if save_connection_ok:
                self.host_edit.clear()
                self.port_nbr.setValue(0)
                self.user_edit.clear()
                self.pass_edit.clear()
                self.db_edit.clear()
        else:
            my_fnc.show_popup(self, 'fields')


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Mysql = QtWidgets.QWidget()
    ui = Ui_SQLServer()
    ui.setupUi(Mysql)
    Mysql.show()
    sys.exit(app.exec_())
