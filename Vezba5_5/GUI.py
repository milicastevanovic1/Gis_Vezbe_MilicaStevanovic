# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vezba_2.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(762, 370)
        self.Btn_connection_db = QtGui.QPushButton(Dialog)
        self.Btn_connection_db.setEnabled(True)
        self.Btn_connection_db.setGeometry(QtCore.QRect(20, 10, 141, 21))
        self.Btn_connection_db.setObjectName(_fromUtf8("Btn_connection_db"))
        self.Btn_citaj_tacke = QtGui.QPushButton(Dialog)
        self.Btn_citaj_tacke.setGeometry(QtCore.QRect(230, 40, 141, 23))
        self.Btn_citaj_tacke.setObjectName(_fromUtf8("Btn_citaj_tacke"))
        self.Btn_citaj_parcele = QtGui.QPushButton(Dialog)
        self.Btn_citaj_parcele.setGeometry(QtCore.QRect(390, 40, 141, 23))
        self.Btn_citaj_parcele.setObjectName(_fromUtf8("Btn_citaj_parcele"))
        self.Box_parceli = QtGui.QGroupBox(Dialog)
        self.Box_parceli.setGeometry(QtCore.QRect(390, 80, 351, 271))
        self.Box_parceli.setObjectName(_fromUtf8("Box_parceli"))
        self.label_oznakaParcele = QtGui.QLabel(self.Box_parceli)
        self.label_oznakaParcele.setGeometry(QtCore.QRect(20, 20, 91, 20))
        self.label_oznakaParcele.setObjectName(_fromUtf8("label_oznakaParcele"))
        self.lineEdit_zaParcele = QtGui.QLineEdit(self.Box_parceli)
        self.lineEdit_zaParcele.setGeometry(QtCore.QRect(110, 20, 131, 20))
        self.lineEdit_zaParcele.setText(_fromUtf8(""))
        self.lineEdit_zaParcele.setObjectName(_fromUtf8("lineEdit_zaParcele"))
        self.Btn_prikazParcele = QtGui.QPushButton(self.Box_parceli)
        self.Btn_prikazParcele.setGeometry(QtCore.QRect(80, 50, 75, 23))
        self.Btn_prikazParcele.setObjectName(_fromUtf8("Btn_prikazParcele"))
        self.label_povrsinaParcele = QtGui.QLabel(self.Box_parceli)
        self.label_povrsinaParcele.setGeometry(QtCore.QRect(30, 90, 301, 20))
        self.label_povrsinaParcele.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_povrsinaParcele.setAutoFillBackground(False)
        self.label_povrsinaParcele.setFrameShape(QtGui.QFrame.StyledPanel)
        self.label_povrsinaParcele.setText(_fromUtf8(""))
        self.label_povrsinaParcele.setObjectName(_fromUtf8("label_povrsinaParcele"))
        self.label_br_prelom = QtGui.QLabel(self.Box_parceli)
        self.label_br_prelom.setGeometry(QtCore.QRect(30, 130, 301, 20))
        self.label_br_prelom.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_br_prelom.setAutoFillBackground(False)
        self.label_br_prelom.setFrameShape(QtGui.QFrame.StyledPanel)
        self.label_br_prelom.setText(_fromUtf8(""))
        self.label_br_prelom.setObjectName(_fromUtf8("label_br_prelom"))
        self.label_koriscenje = QtGui.QLabel(self.Box_parceli)
        self.label_koriscenje.setGeometry(QtCore.QRect(30, 170, 301, 20))
        self.label_koriscenje.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_koriscenje.setAutoFillBackground(False)
        self.label_koriscenje.setFrameShape(QtGui.QFrame.StyledPanel)
        self.label_koriscenje.setText(_fromUtf8(""))
        self.label_koriscenje.setObjectName(_fromUtf8("label_koriscenje"))
        self.label_wkt_parcela = QtGui.QLabel(self.Box_parceli)
        self.label_wkt_parcela.setGeometry(QtCore.QRect(30, 210, 301, 41))
        self.label_wkt_parcela.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_wkt_parcela.setAutoFillBackground(False)
        self.label_wkt_parcela.setFrameShape(QtGui.QFrame.StyledPanel)
        self.label_wkt_parcela.setText(_fromUtf8(""))
        self.label_wkt_parcela.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_wkt_parcela.setWordWrap(True)
        self.label_wkt_parcela.setObjectName(_fromUtf8("label_wkt_parcela"))
        self.Box_tacki = QtGui.QGroupBox(Dialog)
        self.Box_tacki.setGeometry(QtCore.QRect(20, 80, 351, 271))
        self.Box_tacki.setObjectName(_fromUtf8("Box_tacki"))
        self.Btn_prikazTacke = QtGui.QPushButton(self.Box_tacki)
        self.Btn_prikazTacke.setGeometry(QtCore.QRect(80, 50, 75, 23))
        self.Btn_prikazTacke.setObjectName(_fromUtf8("Btn_prikazTacke"))
        self.lineEdit_zaTacku = QtGui.QLineEdit(self.Box_tacki)
        self.lineEdit_zaTacku.setGeometry(QtCore.QRect(110, 20, 131, 20))
        self.lineEdit_zaTacku.setText(_fromUtf8(""))
        self.lineEdit_zaTacku.setObjectName(_fromUtf8("lineEdit_zaTacke"))
        self.label_X = QtGui.QLabel(self.Box_tacki)
        self.label_X.setGeometry(QtCore.QRect(40, 130, 281, 20))
        self.label_X.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_X.setAutoFillBackground(False)
        self.label_X.setFrameShape(QtGui.QFrame.StyledPanel)
        self.label_X.setText(_fromUtf8(""))
        self.label_X.setObjectName(_fromUtf8("label_X"))
        self.label_oznakaTacke = QtGui.QLabel(self.Box_tacki)
        self.label_oznakaTacke.setGeometry(QtCore.QRect(30, 20, 81, 20))
        self.label_oznakaTacke.setObjectName(_fromUtf8("label_oznakaTacke"))
        self.label_wkt_tacke = QtGui.QLabel(self.Box_tacki)
        self.label_wkt_tacke.setGeometry(QtCore.QRect(40, 210, 281, 20))
        self.label_wkt_tacke.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_wkt_tacke.setAutoFillBackground(False)
        self.label_wkt_tacke.setFrameShape(QtGui.QFrame.StyledPanel)
        self.label_wkt_tacke.setText(_fromUtf8(""))
        self.label_wkt_tacke.setAlignment(QtCore.Qt.AlignCenter)
        self.label_wkt_tacke.setObjectName(_fromUtf8("label_wkt_tacke"))
        self.label_Y = QtGui.QLabel(self.Box_tacki)
        self.label_Y.setGeometry(QtCore.QRect(40, 90, 281, 20))
        self.label_Y.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_Y.setAutoFillBackground(False)
        self.label_Y.setFrameShape(QtGui.QFrame.StyledPanel)
        self.label_Y.setText(_fromUtf8(""))
        self.label_Y.setObjectName(_fromUtf8("label_Y"))
        self.label_ucestvuje = QtGui.QLabel(self.Box_tacki)
        self.label_ucestvuje.setGeometry(QtCore.QRect(40, 170, 281, 20))
        self.label_ucestvuje.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_ucestvuje.setAutoFillBackground(False)
        self.label_ucestvuje.setFrameShape(QtGui.QFrame.StyledPanel)
        self.label_ucestvuje.setText(_fromUtf8(""))
        self.label_ucestvuje.setObjectName(_fromUtf8("label_ucestvuje"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Vezba 2", None))
        self.Btn_connection_db.setText(_translate("Dialog", "Konekcije sa bazom", None))
        self.Btn_citaj_tacke.setText(_translate("Dialog", "Ucitaj tacke", None))
        self.Btn_citaj_parcele.setText(_translate("Dialog", "Ucitaj parcele", None))
        self.Box_parceli.setTitle(_translate("Dialog", "Parcela", None))
        self.label_oznakaParcele.setText(_translate("Dialog", "Oznaka parcele:", None))
        self.Btn_prikazParcele.setText(_translate("Dialog", "Prikazi", None))
        self.Box_tacki.setTitle(_translate("Dialog", "Detaljne tacke", None))
        self.Btn_prikazTacke.setText(_translate("Dialog", "Prikazi", None))
        self.label_oznakaTacke.setText(_translate("Dialog", "Oznaka tacke:", None))

