from DetaljnaTacka import DetaljnaTacka
from Parcela import Parcela
from Poligon import Poligon
from GUI import *
from PyQt4.QtGui import *
import pypyodbc
import sys
import psycopg2


class callGUI (QDialog, Ui_Dialog):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.connection=None
        self.lista_tacaka = []
        self.lista_parcela = []

        self.connect(self.ui.Btn_connection_db, QtCore.SIGNAL('clicked()'), self.db_connection)
        self.connect(self.ui.Btn_citaj_tacke, QtCore.SIGNAL('clicked()'), self.citajTacke)
        self.connect(self.ui.Btn_citaj_parcele, QtCore.SIGNAL('clicked()'), self.citajParcele)
      
        self.connect(self.ui.Btn_prikazParcele, QtCore.SIGNAL('clicked()'), self.Parcela_deo)
        self.connect(self.ui.lineEdit_zaParcele, QtCore.SIGNAL('clicked()'), self.Parcela_deo)

        self.connect(self.ui.Btn_prikazTacke, QtCore.SIGNAL('clicked()'), self.DetaljneTacke_deo)
        self.connect(self.ui.lineEdit_zaTacku, QtCore.SIGNAL('clicked()'), self.DetaljneTacke_deo)


    def db_connection(self):
        try:
            self.connection =  psycopg2.connect("dbname='postgis_baza' user='postgres' host='localhost' password='admin'")
            QMessageBox.information(self, "Done", "Uspesno povezano sa bazom.")

        except:
            print "I am unable to connect to the database"

    def citajParcele(self):
        kursor = self.connection.cursor()
        kursor.execute("SELECT * FROM Parcele") 
        
        for i, r in enumerate(kursor.fetchall()):
            self.lista_parcela.append(Parcela(i + 1, [], r[0], r[1], r[2]))

        for n in self.lista_parcela:
             kursor.execute("SELECT id_detaljne_tacke FROM Parcele_DTacke WHERE id_parcela=%s" % n.get_id_parcela())
             lista_prelomnih = []

             for red in kursor.fetchall():
                 lista_prelomnih.append(red[0])
             for p in self.lista_tacaka:
                 if p.get_id_detaljne_tacke() in lista_prelomnih:
                     n.get_prelomne_tacke().append(p)

        kursor.close()
        QMessageBox.information(self,"Done","Uspesno ucitane parcele.")


    def citajTacke(self):
        kursor = self.connection.cursor()
        kursor.execute ("SELECT * FROM detaljne_tacke")
        for r in kursor.fetchall():
            self.lista_tacaka.append(DetaljnaTacka(r[0], r[1], r[2], r[3], r[4]))
        kursor.close()
        QMessageBox.information(self,"Done","Uspesno ucitane tacke.")


    def Parcela_deo(self):
        trazena_parcela = None
        ulaz = self.ui.lineEdit_zaParcele.text()
        for i in self.lista_parcela:
            br_parcele = str(i.get_br_parcela())
            if br_parcele == ulaz:
                trazena_parcela = i
        if trazena_parcela is None: QMessageBox.warning(self,"Error", "Nema takve parcele, pokusajte ponovo.")
        else:
            self.ui.label_povrsinaParcele.setText("Area: {0:1f}".format(trazena_parcela.polygonArea()))
            self.ui.label_br_prelom.setText("Broj prelomnih tacaka: %s " % trazena_parcela.br_prelomne_tacke())
            self.ui.label_koriscenje.setText("Nacin koriscenja: %s " % trazena_parcela.daj_nacin_koriscenja())
            self.ui.label_wkt_parcela.setText("WKT geometrija: %s " % trazena_parcela.get_wkt_poligon())

    def DetaljneTacke_deo (self):
        trazena_tacka = None
        ulaz = self.ui.lineEdit_zaTacku.text()
        for i in self.lista_tacaka:
            oznaka = str(i.get_oznaka_tacke())
            if oznaka == ulaz: trazena_tacka = i
        if trazena_tacka is None: QMessageBox.warning(self,"Error","Nema takve tacke, pokusajte ponovo.")
        else:
            u = "Ne ucestvuje u parcelama ili nisu ucitane parcele"
            for n in self.lista_parcela:
                if trazena_tacka in n.get_prelomne_tacke():
                    u = "Ucestvuje u parceli."
                    break
                else: u = "Ne ucestvuje u parceli."
            self.ui.label_Y.setText("Y = %s" % trazena_tacka.get_y())
            self.ui.label_X.setText("X = %s" % trazena_tacka.get_x())
            self.ui.label_ucestvuje.setText(u)
            self.ui.label_wkt_tacke.setText("WKT geometrija: %s " % trazena_tacka.get_wkt_tacke())

app = QApplication(sys.argv)
form = callGUI()
form.show()
app.exec_()
