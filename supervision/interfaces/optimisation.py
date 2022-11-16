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



labels = []
boutons = []
layout_lbs = []
IP = "192.168.1.1"

class Interface(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Terminal")
        self.resize(600,600)
        self.group72 = QGroupBox()
        self.grid = QGridLayout()
        self.verticale = QVBoxLayout(self.group72)
        self.baroutils = QToolBar()
        self.IP = QLabel(IP)
        self.etat = QLabel("off")
        if IP != "":
            self.etat.setText("on")

        
        self.off = QAction(QIcon("off.png"),"OFF",self)
        self.off.setStatusTip("OFF")
        self.baroutils.addAction(self.off)
        self.baroutils.setIconSize(QSize(50,50))
        self.envoyer = QPushButton("Envoyer")
        self.envoyer.setFixedSize(100,30)
        self.grid.addWidget(self.etat, 0, 0)
        self.grid.addWidget(self.IP,0,1)
        self.grid.addWidget(self.envoyer,0,4)
        self.commande = QTextEdit()
        self.commande.setStyleSheet("color: white; background: rgba(56, 4, 40, 0.9)")
        self.verticale.addLayout(self.grid)
        self.verticale.addWidget(self.commande)
        
        
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
        self.labels = []
        for i in range(6):
            for j in range(4):
                label,bouton,layout_lb = self.create_bouton(str(i))
                labels.append(label)
                boutons.append(bouton)
                layout_lbs.append(layout_lb)
                self.grid.addLayout(layout_lbs[i], i, j)

        
        self.setCentralWidget(self.group)
    
    def create_bouton(self,titre_label):
        label = QLabel("PC"+titre_label+"   IP : "+IP)
        bouton = QPushButton()
        bouton.setIcon(QIcon("/root/SA-302/supervision/interfaces/images/pc.png"))
        bouton.setIconSize(QSize(110,110))
        bouton.clicked.connect(self.page)
        layout_lb = QVBoxLayout(self.group)
        layout_lb.addWidget(label)
        layout_lb.addWidget(bouton)
        return label,bouton,layout_lb
        
    
    def page(self):
        self.newpage = Interface()
        self.newpage.show()
    

def main():
    application = QApplication(sys.argv)
    mon_appli = Supervision()
    mon_appli.show()
    sys.exit(application.exec_())


if __name__== '__main__':
    main()
    
""" 
self.l1 = QLabel("                                   PC1 | IP = 192.168.56.1")
self.b1 = QPushButton()
self.b1.setIcon(QIcon("pc.png"))
self.b1.setIconSize(QSize(110,110))
self.b1.clicked.connect(self.page)
self.l1b1 = QVBoxLayout(self.group)
self.l1b1.addWidget(self.l1)
self.l1b1.addWidget(self.b1)
self.l2 = QLabel("                                   PC1 | IP = 192.168.56.1")
self.b2 = QPushButton()
self.b2.setIcon(QIcon("pc.png"))
self.b2.setIconSize(QSize(110,110))
self.b2.clicked.connect(self.page)
self.l2b2 = QVBoxLayout(self.group)
self.l2b2.addWidget(self.l2)
self.l2b2.addWidget(self.b2)
"""
