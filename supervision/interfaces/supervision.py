#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 13:17:15 2022

@author: etudiant
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QSize


PC = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
IP = "192.168.1.1"


class Interface(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Terminal")
        self.resize(600,600)
        self.baroutils = QToolBar()
        self.onglet = QTabWidget()
        self.add_onglet()
        self.plus_onglet = QAction(QIcon("/home/etudiant/Téléchargements/SA-302-main(1)/SA-302-main/supervision/interfaces/images/plus.png"), "Nouvel Onglet",self)
        self.plus_onglet.setStatusTip("Nouvel Onglet")
        self.plus_onglet.triggered.connect(self.nouvel_onglet)
        self.baroutils.addAction(self.plus_onglet)
        for i in range(10):
            vide = self.creervide()
            self.baroutils.addAction(vide)
        self.off = QAction(QIcon("/home/etudiant/Téléchargements/SA-302-main(1)/SA-302-main/supervision/interfaces/images/off.png"),"OFF",self)
        self.off.setStatusTip("OFF")
        self.off.triggered.connect(self.eteint)
        self.baroutils.addAction(self.off)
        self.baroutils.setIconSize(QSize(39,30))
        self.addToolBar(self.baroutils)
        self.setCentralWidget(self.onglet)
        
        
    def creervide(self):
        self.vide = QAction(QIcon(""),"",self)
        return self.vide
    
    def add_onglet(self,widget=None,label="Terminal"):
        self.group72 = QGroupBox()
        self.grid = QGridLayout()
        self.verticale = QVBoxLayout(self.group72)
        self.fenetre = QVBoxLayout()
        self.IP = QLabel(IP)
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

    def nouvel_onglet(self):
        self.add_onglet()
        
    def eteint(self):
        self.etat.setText("off")
        self.IP.setText("")
        self.close()
    
class Supervision(QMainWindow):
    
    
    def __init__(self,nb_pc = 24):
        super().__init__()
        self.setWindowTitle("Supervision")
        self.resize(800,800)
        self.setWindowIcon(QIcon("/home/etudiant/Téléchargements/SA-302-main(1)/SA-302-main/supervision/interfaces/images/logo.png"))
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
        bouton.setIcon(QIcon("/home/etudiant/Téléchargements/SA-302-main(1)/SA-302-main/supervision/interfaces/images/pc.png"))
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
    
