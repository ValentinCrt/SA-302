#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 10:33:46 2022

@author: etudiant
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QGroupBox, QWidget, QHBoxLayout
from PyQt5.QtWidgets import QMenu, QAction, QTextEdit, QMenuBar, QToolBar, QGridLayout, QLineEdit, QMessageBox, QInputDialog
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QSize



PC = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
IP = "192.168.1.1"
#GRILLE = [[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15],[16,17,18,19],[20,21,22,23]]
NUM_TERM = ''

class Interface(QMainWindow):
    
    def __init__(self):
        super().__init__()
        print(NUM_TERM)
        self.setWindowTitle("Terminal_"+NUM_TERM)
        self.resize(600,600)
        self.group72 = QGroupBox()
        self.grid = QGridLayout()
        self.verticale = QVBoxLayout(self.group72)
        self.baroutils = QToolBar()
        self.IP = QLabel(IP)
        self.etat = QLabel("off")
        if IP != "":
            self.etat.setText("on")
        self.commande = QTextEdit()
        self.commande.setStyleSheet("color: white; background: rgba(56, 4, 40, 0.9)")
        self.reponse = QTextEdit()
        self.reponse.setStyleSheet("color: white; background: rgba(56, 4, 40, 0.9)")
        self.reponse.setReadOnly(True)

        
        self.off = QAction(QIcon("/SA-302/supervision/interfaces/images/off.png"),"OFF",self)
        self.off.setStatusTip("OFF")
        self.baroutils.addAction(self.off)
        self.baroutils.setIconSize(QSize(50,50))
        self.envoyer = QPushButton("Envoyer")
        self.envoyer.setFixedSize(100,30)
        self.grid.addWidget(self.etat, 0, 0)
        self.grid.addWidget(self.IP,0,1)
        self.grid.addWidget(self.envoyer,0,4)
        self.verticale.addLayout(self.grid)
        self.verticale.addWidget(self.commande)
        self.verticale.addWidget(self.reponse)
        

        
        self.addToolBar(self.baroutils)
        self.setCentralWidget(self.group72)
        
class Supervision(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Supervision")
        self.resize(800,800)
        self.setWindowIcon(QIcon("/root/SA-302/supervision/interfaces/images/pc.png"))
        self.group = QGroupBox()
        self.grid = QGridLayout(self.group)
        self.group.setLayout(self.grid)
        self.setCentralWidget(self.group)

        Y = 0
        self.windows = []
        for i in range(6):
            for j in range(4):
                layout_lb = self.create_bouton(str(PC[Y]))
                Y+=1
                self.grid.addLayout(layout_lb, i, j)
    
    def create_bouton(self,titre_label):
        label = QLabel("PC"+titre_label+"   IP : "+IP)
        bouton = QPushButton()
        bouton.setIcon(QIcon("/root/SA-302/supervision/interfaces/images/pc.png"))
        bouton.setIconSize(QSize(70,70))
        bouton.clicked.connect(self.page)
        layout_lb = QVBoxLayout()
        layout_lb.addWidget(label)
        layout_lb.addWidget(bouton)
        return layout_lb
        
    
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
    
