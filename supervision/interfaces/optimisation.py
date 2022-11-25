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

    
#Création de la classe Supervision qui affiche les PC supervisés
class Supervision(QMainWindow):
    
    def __init__(self):
        
        super().__init__()
        
        #Ajout d'un titre au logiciel
        self.setWindowTitle("Supervision")
        #Fixe la taille du logiciel
        self.resize(800,800)
        #Définit le logo du logiciel
        self.setWindowIcon(QIcon("images/logo.png"))
        
    
        #Création des zones
        
        #Création d'un groupe
        self.group = QGroupBox()
        #Ajout du groupe dans la fenêtre
        self.setCentralWidget(self.group)
        
        #Création d'une grille et Ajout de la grille dans le groupe
        self.grid = QGridLayout(self.group)
        
        #Rattacher les futurs interfaces dans la fenêtre
        self.windows = []
        
        #Création des Boutons dans la grille
        Y = 0
        #Nombre de colonnes
        for i in range(6):
            #Nombre de lignes
            for j in range(4):
                layout_lb = self.create_bouton(str(PC[Y]))
                Y+=1
                self.grid.addLayout(layout_lb, i, j)
                
    
    
    #Méthode de création des boutons
    def create_bouton(self,titre_label):
        
        #Création d'un label
        label = QLabel("PC"+titre_label+"   IP : "+IP)
        
        #Création du bouton
        bouton = QPushButton()
        bouton.setIcon(QIcon("images/pc.png"))
        bouton.setIconSize(QSize(70,70))
        bouton.clicked.connect(self.page) #lien qui relie le bouton à la fonction qui appelle l'interface
        
        #Création d'un layout verticale et Ajout du label et du bouton
        layout_lb = QVBoxLayout()
        layout_lb.addWidget(label)
        layout_lb.addWidget(bouton)
        
        return layout_lb
        
        
     
    #Méthode qui appelle et affiche la classe interface
    def page(self):
        
        window = Interface()
        self.windows.append(window) #Attache la fenêtre interface à la fenêtre supervision
        window.show()

class Interface(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        
        #Ajout d'un titre au logiciel
        self.setWindowTitle("Terminal")
        #Fixe la taille du logiciel
        self.resize(600,600)
        
        
        #Création des zones
        
        #Création d'une barre d'outils
        self.baroutils = QToolBar()
        
        self.onglet = QTabWidget()
        self.add_onglet()
        self.plus_onglet = QAction(QIcon("images/plus.png"), "Nouvel Onglet",self)
        self.plus_onglet.setStatusTip("Nouvel Onglet")
        self.plus_onglet.triggered.connect(self.add_onglet)
        self.baroutils.addAction(self.plus_onglet)
        for i in range(10):
            vide = self.creervide()
            self.baroutils.addAction(vide)
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
    
    def add_onglet(self,widget=None,label="Terminal"):
        
        #Création d'un groupe
        self.groupe_terminal = QGroupBox()
        #Création d'un layout verticale et Ajout du layout verticale dans le groupe
        self.verticale = QVBoxLayout(self.groupe_terminal)
        
        
        #Création d'un layout verticale et Ajout du layout verticale dans le groupe
        self.fenetre = QVBoxLayout()
        self.fenetre.addWidget(self.groupe_terminal)
        #Création de la grille
        self.grid = QGridLayout()
        
        self.IP = QLabel(IP)
        self.etat = QLabel("off")
        if IP != "":
            self.etat.setText("on")
        self.envoyer = QPushButton("Envoyer")
        self.envoyer.setFixedSize(110,30)
        
        #Ajout de l'IP, de l'état ,du boutton envoyer dans la grille
        self.grid.addWidget(self.etat, 0, 0)
        self.grid.addWidget(self.IP,0,1)
        self.grid.addWidget(self.envoyer,0,4)

        #Création du bloc commande
        self.commande = QTextEdit()
        self.commande.setStyleSheet("color: white; background: rgba(56, 4, 40, 0.9)")
        
        #Création du bloc réponse
        self.reponse = QTextEdit()
        self.reponse.setStyleSheet("color: white; background: rgba(56, 4, 40, 0.9)")
        self.reponse.setReadOnly(True)
        
        #Création d'un widget du nouvel onglet
        self.widget = QWidget()
        self.widget.setLayout(self.fenetre)
        
        num_onglet = self.onglet.addTab(self.widget,label)
        self.onglet.setCurrentIndex(num_onglet)

        
        #Ajout de la grille, du bloc commande, du bloc réponse dans le layout verticale
        self.verticale.addLayout(self.grid)
        self.verticale.addWidget(self.commande)
        self.verticale.addWidget(self.reponse)
        
    
        
    def eteint(self):
        self.etat.setText("off")
        self.IP.setText("")
        self.close()
        
        

#Création de la fonction main qui va lancer le logiciel
def main():
    application = QApplication(sys.argv)
    mon_appli = Supervision()
    mon_appli.show()
    sys.exit(application.exec_())

#Appelle de la fonction main
if __name__== '__main__':
    main()
