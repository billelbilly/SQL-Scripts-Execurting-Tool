# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'import_script.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!
import os
import re
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
import functions as my_fnc
from dbConnection import db_connection


class Ui_import_script(object):
    script_path = ""
    # select_type_db_val = ""
    # select_version_val = ""
    query = ""



    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowIcon(QIcon('iconBig.gif'))
        # Form.resize(457, 350)
        Form.setFixedSize(457, 212)
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
        Form.setPalette(palette)
        self.btn_import = QtWidgets.QPushButton(Form)
        self.btn_import.setGeometry(QtCore.QRect(30, 60, 75, 23))
        self.btn_import.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_import.setStyleSheet("QPushButton:hover:!pressed\n"
                                      "{\n"
                                      "  border: 1px solid lime;\n"
                                      "background-color: rgb(0, 0, 0);\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton\n"
                                      "{\n"
                                      "background-color: rgb(0, 0, 0);\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "padding:2px;\n"
                                      "}")
        self.btn_import.setObjectName("btn_import")
        self.import_field = QtWidgets.QLineEdit(Form)
        self.import_field.setGeometry(QtCore.QRect(140, 60, 291, 21))
        self.import_field.setObjectName("import_field")
        self.import_field.setReadOnly(True)
        # self.select_version = QtWidgets.QComboBox(Form)
        # self.select_version.setGeometry(QtCore.QRect(230, 120, 141, 21))
        # self.select_version.setObjectName("select_version")
        # self.select_type_db = QtWidgets.QComboBox(Form)
        # self.select_type_db.setGeometry(QtCore.QRect(230, 160, 141, 21))
        # self.select_type_db.setObjectName("select_type_db")
        # self.select_type_db.addItem("")
        # self.select_type_db.addItem("")
        # self.select_version_label = QtWidgets.QLabel(Form)
        # self.select_version_label.setGeometry(QtCore.QRect(30, 120, 141, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        # self.select_version_label.setPalette(palette)
        # self.select_version_label.setObjectName("select_version_label")
        # self.type_db_label = QtWidgets.QLabel(Form)
        # self.type_db_label.setGeometry(QtCore.QRect(30, 160, 91, 16))
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
        # self.type_db_label.setPalette(palette)
        # self.type_db_label.setObjectName("type_db_label")
        self.btn_save = QtWidgets.QPushButton(Form)
        self.btn_save.setGeometry(QtCore.QRect(140, 130, 120, 31))
        self.btn_save.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_save.setStyleSheet("QPushButton:hover:!pressed\n"
                                    "{\n"
                                    "  border: 1px solid lime;\n"
                                    "background-color: rgb(0, 0, 0);\n"
                                    "font: 28 12pt \"Cambria\";\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton\n"
                                    "{\n"
                                    "background-color: rgb(0, 0, 0);\n"
                                    "font: 28 12pt \"Cambria\";\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "padding:2px;\n"
                                    "}")
        self.btn_save.setObjectName("btn_save")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        "my view changes"
        self.btn_save.setIcon(QIcon('Save_16x16.png'))
        self.btn_save.setIconSize(QSize(16, 16))
        # self.select_version_val = str(self.select_version.currentText())
        # self.select_type_db_val = str(self.select_type_db.currentText())

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Scripts Tool V1.0.0"))
        self.btn_import.setText(_translate("Form", "Parcourir ..."))
        # self.select_type_db.setItemText(0, _translate("Form", "SqlServer"))
        # self.select_type_db.setItemText(1, _translate("Form", "MySql"))
        # self.select_version_label.setText(_translate("Form", "Sélectionner Version:"))
        # self.type_db_label.setText(_translate("Form", "Type Script:"))
        self.btn_save.setText(_translate("Form", "Enregistrer"))

        """  my logic """
        # self.populate_version()
        self.btn_save.clicked.connect(self.save_to_db)
        self.btn_import.clicked.connect(self.upload_file)

        # self.select_type_db.currentTextChanged.connect(self.get_type_db)
        # self.select_version.currentTextChanged.connect(self.get_version)

    # def populate_version(self):
    #     # self.select_version.clear()
    #     list_version = my_fnc.list_version()
    #
    #     for i in list_version:
    #         self.select_version.addItem(str(i[-1]))

    def upload_file(self):
        dialog = QtWidgets.QFileDialog()
        dir_path = dialog.getExistingDirectory(None, 'Sélectionnez Dossier Version')
        self.import_field.setText(dir_path.replace('/','\\'))



    # def get_version(self):
    #     self.select_version_val = str(self.select_version.currentText())
    #
    # def get_type_db(self):
    #     self.select_type_db_val = str(self.select_type_db.currentText())

    def save_to_db(self):

        script_upload = self.import_field.text()
        if script_upload != "":

            script_ok=my_fnc.save_scripts(script_upload)
            # my_fnc.test_popup()

            if script_ok:
                my_fnc.show_popup_script()
            else:
                my_fnc.admin('SVP Lancer l\'application En tant qu\'Administrateur '
                                 'pour que vous puissiez soumettre vos changement à la base de donnée !')

        else:
            my_fnc.import_script_svp()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_import_script()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
