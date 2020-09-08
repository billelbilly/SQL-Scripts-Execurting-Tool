# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'import_script_final.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
import functions as my_fnc
from dbConnection import db_connection


class Ui_import_script(object):
    script_path = ""
    select_type_db_val = ""
    select_version_val = ""
    query = ""


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(457, 212)
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
        self.btn_save = QtWidgets.QPushButton(Form)
        self.btn_save.setGeometry(QtCore.QRect(140, 130, 101, 31))
        self.btn_save.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_save.setStyleSheet("QPushButton:hover:!pressed\n"
"{\n"
"  border: 1px solid lime;\n"
"background-color: rgb(0, 0, 0);\n"
"font: 75 14pt \"Cambria\";\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"background-color: rgb(0, 0, 0);\n"
"font: 75 14pt \"Cambria\";\n"
"color: rgb(255, 255, 255);\n"
"padding:2px;\n"
"}")
        self.btn_save.setObjectName("btn_save")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn_import.setText(_translate("Form", "Parcourir ..."))
        self.btn_save.setText(_translate("Form", "Enregistrer"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())