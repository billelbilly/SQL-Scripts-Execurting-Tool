# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about_big.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon


class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName("About")
        About.setWindowIcon(QIcon('Information_16x16.png'))
        # About.resize(575, 397)
        About.setFixedSize(575, 397)
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
        About.setPalette(palette)
        self.label = QtWidgets.QLabel(About)
        self.label.setGeometry(QtCore.QRect(190, 30, 200, 200))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("big.png"))
        self.label.setObjectName("label")
        # self.textBrowser = QtWidgets.QTextBrowser(About)
        # self.textBrowser.setGeometry(QtCore.QRect(10, 260, 551, 101))
        # self.textBrowser.setObjectName("textBrowser")

        self.label_version = QtWidgets.QLabel(About)
        self.label_version.setGeometry(QtCore.QRect(40, 80, 200, 100))
        self.label_version.setText("        Script Tool V1.0.1\nCopyright © BigInformatique")
        self.label_version.setObjectName("label_version")
        self.label_version.setStyleSheet("""QLabel{color:white;}""")



        self.retranslateUi(About)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        _translate = QtCore.QCoreApplication.translate
        About.setWindowTitle(_translate("About", "à propos"))
#         self.textBrowser.setHtml(_translate("About", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
# "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
# "p, li { white-space: pre-wrap; }\n"
# "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
# "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; color:#1487d4;\">Siège Social: </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\">Les Santons III N° 6 Annaba Algérie </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; color:#1487d4;\">Tél/Fax: </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\">(+213) 0 38 45 21 55/56 </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; color:#1487d4;\">Mob: </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\">(+213) 0 770 94 57 85<br /></span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; color:#1487d4;\">Annaba: </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\">Sidi Aissa Villa N°5 </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; color:#1487d4;\">Tél: </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\">038 55 91 00 / 038 55 91 02 </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; color:#1487d4;\"><br />Fax: </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\">038 45 21 56<br /></span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; color:#1487d4;\">Alger: </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\">Rue n°2 Villa n°7, Les Vergers, Bir Mourad Rais Alger Algérie </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; color:#1487d4;\">Tél: </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\">0 23 52 51 78 /023 52 51 67 FAX : 0 23 52 51 68 <br /></span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; color:#1487d4;\">Oran: </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\">42 Rue de Balzac bon Accueil Oran Algérie </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; color:#1487d4;\">Tél: </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\">00213 41 82 50 34/ 41 82 51 22 </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; color:#1487d4;\">Fax: </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\">00213 41 82 50 34<br /></span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; color:#1487d4;\">big@biginformatique.com</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\"> </span></p></body></html>"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    About = QtWidgets.QWidget()
    ui = Ui_About()
    ui.setupUi(About)
    About.show()
    sys.exit(app.exec_())
