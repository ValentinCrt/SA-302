#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 13:24:13 2022

@author: etudiant
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 13:17:15 2022

@author: etudiant
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QSize
from pyqt_tab_widget import TabWidget

PC = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
IP = ["192.168.89.19","192.168.89.20","192.168.89.21","192.168.89.22","192.168.89.23","192.168.89.24",
      "192.168.89.13","192.168.89.14","192.168.89.15","192.168.89.16","192.168.89.17","192.168.89.18",
      "192.168.89.7","192.168.89.8","192.168.89.9","192.168.89.10","192.168.89.11","192.168.89.12",
      "192.168.89.1","192.168.89.2","192.168.89.3","192.168.89.4","192.168.89.5","192.168.89.6"]

class Interface(QMainWindow):
    
    def __init__(self, ip):
        super().__init__()
        self.ip = ip
        self.setWindowTitle("Terminal")
        self.resize(600,600)
        self.menubar = self.menuBar()
        self.baroutils = QToolBar()
        self.onglet = TabWidget()
        self.plus_onglet = QAction(QIcon("images/plus.png"), "Nouvel Onglet",self)
        self.plus_onglet.setStatusTip("Nouvel Onglet")
        self.plus_onglet.triggered.connect(self.add_onglet)
        self.baroutils.addAction(self.plus_onglet)
        self.windows = []
        self.onglets = []
        self.add_onglet()
        for i in range(10):
            vide = self.creervide()
            self.baroutils.addAction(vide)
            
        self.fichier = self.menubar.addMenu("Fichier")
        self.ouvrir = QAction(QIcon("images/ouvrir.png"), "Ouvrir", self)
        self.ouvrir.setShortcut("Ctrl+O")
        self.fichier.addAction(self.ouvrir)
        self.ouvrir.triggered.connect(self.open_event)
        self.off = QAction(QIcon("images/off.png"),"OFF",self)
        self.off.setStatusTip("OFF")
        self.off.triggered.connect(self.eteint)
        self.baroutils.addAction(self.off)
        self.baroutils.setIconSize(QSize(39,30))
        self.addToolBar(self.baroutils)
        self.setCentralWidget(self.onglet)
        
        
    def creervide(self):
        self.vide = QAction(QIcon(""),"",self)
        return self.vide

    def open_event(self):
            dossier = QFileDialog.getOpenFileName(self)
            fichier = open(dossier[0]).read()
            self.commande.append(fichier)

    def add_onglet(self,widget=None,label="Terminal"):
        self.group72 = QGroupBox()
        self.grid = QGridLayout()
        self.verticale = QVBoxLayout(self.group72)
        self.fenetre = QVBoxLayout()
        self.IP = QLabel(self.ip.text())
        self.etat = QLabel("off")
        self.widget = QWidget()
        if IP != "":
            self.etat.setText("on")
        self.commande = QTextEdit()
        self.commande.setStyleSheet("color: white; background: rgba(56, 4, 40, 0.9)")
        self.reponse = QTextEdit()
        self.reponse.setStyleSheet("color: white; background: rgba(56, 4, 40, 0.9)")
        self.reponse.setReadOnly(True)
        self.envoyer = QPushButton("Envoyer")
        self.envoyer.clicked.connect(self.send)
        self.envoyer.setFixedSize(110,30)
        self.grid.addWidget(self.etat, 0, 0)
        self.grid.addWidget(self.IP,0,1)
        self.grid.addWidget(self.envoyer,0,8)
        self.verticale.addLayout(self.grid)
        self.verticale.addWidget(self.commande)
        self.verticale.addWidget(self.reponse)
        self.fenetre.addWidget(self.group72)
        self.widget.setLayout(self.fenetre)
        self.onglets.append(self.widget)
        self.onglet.addTab( self.onglets[-1] , 'Page %s' % len(self.onglets) )
        self.onglet.setCurrentIndex( len(self.onglets)-1 )
        
        
    def send(self):
        envoyer = Envoyer()
        self.windows.append(envoyer)
        envoyer.show()
        
    
    def eteint(self):
        self.etat.setText("off")
        self.IP.setText("")
        self.close()
        
    def fermer_onglet(self):
        self.onglet.removeTab()
    
class Supervision(QMainWindow):
    
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Supervision")
        self.resize(800,800)
        self.setWindowIcon(QIcon("images/logo.png"))
        self.group = QGroupBox()
        self.grid = QGridLayout(self.group)
        self.setCentralWidget(self.group)
        self.windows = []
        self.create_bouton()
            
        
    
    def create_bouton(self):
        self.Y = 0
        for i in range(4):
            for j in range(6):
                self.label = QLabel("PC"+str(PC[self.Y])+"   IP : "+IP[self.Y])
                self.bouton = QPushButton()
                self.bouton.setIcon(QIcon("images/pc.png"))
                self.bouton.setIconSize(QSize(70,70))
                self.bouton.clicked.connect(self.page)
                self.layout_lb = QVBoxLayout()
                self.layout_lb.addWidget(self.label)
                self.layout_lb.addWidget(self.bouton)
                self.Y+=1
                self.grid.addLayout(self.layout_lb, i, j)


        
        self.setCentralWidget(self.group)
        
        
        
    def page(self):
        for i in range(6):
            for j in range(4):
               if self.grid.itemAtPosition(i, j).itemAt(1).widget() == self.bouton.sender():
                   ip = self.grid.itemAtPosition(i, j).itemAt(0).widget()
        window = Interface(ip)
        self.windows.append(window)
        window.show()
        
        
class Envoyer(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Envoyer")
        self.resize(400,400)
        self.setWindowIcon(QIcon("images/envoyer.png"))
        self.group = QGroupBox()
        self.grille = QGridLayout(self.group)
        self.bsend = QPushButton(self.group)
        self.bsend.setIcon(QIcon("images/envoyer.png"))
        self.bsend.setIconSize(QSize(30,30))
        self.bsend.setFixedSize(40, 40)
        self.bsend.move(175,360)
        self.bsend.clicked.connect(self.sends)
        Y=0
        for i in range(6):
            for j in range(4):
                self.grille.addWidget(QCheckBox("PC"+str(PC[Y])), i, j)
                Y+=1
        
        self.setCentralWidget(self.group)
        

        
    def sends(self):
        for i in range(6):
            for j in range(4):
                print(self.grille.itemAtPosition(i, j).widget().isChecked())
                print(Interface().IP)

                    
        
def main():
    application = QApplication(sys.argv)
    mon_appli = Supervision()
    mon_appli.show()
    sys.exit(application.exec_())


if __name__== '__main__':
    main()
    
