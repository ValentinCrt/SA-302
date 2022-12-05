#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
.. module::supervision
   :platform: Unix
   :synopsis: this module is the interface, connections and controller together
  
.. moduleauthor:: Duquerroy Léonce <leonce.duquerroy@etu.univ-poitiers.fr>
.. moduleauthor:: Etiembre Baptiste <baptiste.etiembre@etu.univ-poitiers.fr>
.. moduleauthor:: Moreau Mathis <mathis.moreau@etu.univ-poitiers.fr>
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QSize
import paramiko
from getpass import getpass
import time

sys.path.insert(0, "../connexion/")

import recuperation_MAC_IP

print(recuperation_MAC_IP.MAC)


PC = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
IP = "192.168.1.1"


class Interface(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Terminal")
        self.resize(600,600)
        self.menubar = self.menuBar()
        self.baroutils = QToolBar()
        self.onglet = QTabWidget()
        self.add_onglet()
        self.plus_onglet = QAction(QIcon("images/plus.png"), "Nouvel Onglet",self)
        self.plus_onglet.setStatusTip("Nouvel Onglet")
        self.plus_onglet.triggered.connect(self.add_onglet)
        self.baroutils.addAction(self.plus_onglet)
        self.windows = []
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

    def add_onglet(self,widget=None,label="Terminal   "):
        self.group72 = QGroupBox()
        self.grid = QGridLayout()
        self.verticale = QVBoxLayout(self.group72)
        self.fenetre = QVBoxLayout()
        self.IP = QLabel(IP)
        self.etat = QLabel("off")
        self.widget = QWidget()
        self.fonglet = QPushButton(self.widget)
        self.fonglet.setText("x")
        self.fonglet.setFixedSize(20,20)
        self.fonglet.clicked.connect(self.fermer_onglet)
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
        self.grid.addWidget(self.envoyer,0,4)
        self.verticale.addLayout(self.grid)
        self.verticale.addWidget(self.commande)
        self.verticale.addWidget(self.reponse)
        self.fenetre.addWidget(self.group72)
        self.widget.setLayout(self.fenetre)
        i = self.onglet.addTab(self.widget,label)
        self.onglet.setCurrentIndex(i)

        
        
    def send(self):
        
        """ this fonction initializes an ssh connection, sends a command to the target pc  and displays the result of the command.
            
        :returns: None
        :rtypes: None
        :raises: NoValidConnectionsError
        
        """

        host = "172.20.35.32"
        username = "etudiant"
        password = "etudiant"

        session = paramiko.SSHClient()
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        session.connect(hostname=host, username=username, password=password, port="22")
        
        commande = self.commande.toPlainText()
        stdin, stdout, stderr =session.exec_command(commande)
        time.sleep(.5)
        reponse = ""+username+"@deb11: \n \n"+str(stdout.read().decode())
        self.reponse.append(reponse)
        
        session.close()
        
    
    def eteint(self):
        self.etat.setText("off")
        self.IP.setText("")
        self.close()
        
    def fermer_onglet(self):
        self.onglet.removeTab(self.onglet.currentIndex())
    
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
        Y = 0
        for i in range(6):
            for j in range(4):
                layout_lb = self.create_bouton(str(PC[Y]))
                Y+=1
                self.grid.addLayout(layout_lb, i, j)
    
    def create_bouton(self,titre_label):
        label = QLabel("PC"+titre_label+"   IP : "+IP)
        bouton = QPushButton()
        bouton.setIcon(QIcon("images/pc.png"))
        bouton.setIconSize(QSize(70,70))
        bouton.clicked.connect(self.page)
        layout_lb = QVBoxLayout()
        layout_lb.addWidget(label)
        layout_lb.addWidget(bouton)
        return layout_lb
        
        
        
        
        
        self.setCentralWidget(self.group)
        
        
    def page(self):
        window = Interface()
        self.windows.append(window)
        window.show()
        

                
        
def main():
    application = QApplication(sys.argv)
    mon_appli = Supervision()
    mon_appli.show()
    sys.exit(application.exec_())


if __name__== '__main__':
    main()
    
