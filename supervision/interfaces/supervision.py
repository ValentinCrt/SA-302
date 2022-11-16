"_version_ = version = 0.2"

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 13:17:15 2022

@author: etudiant
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QGroupBox, QWidget, QHBoxLayout
from PyQt5.QtWidgets import QMenu, QAction, QTextEdit, QMenuBar, QToolBar, QGridLayout, QLineEdit, QMessageBox, QInputDialog
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QSize


IP = ""

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
        self.setWindowIcon(QIcon("logo.png"))
        self.group = QGroupBox()
        self.grid = QGridLayout(self.group)
        
        
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
        self.l3 = QLabel("                                   PC1 | IP = 192.168.56.1")
        self.b3 = QPushButton()
        self.b3.setIcon(QIcon("pc.png"))
        self.b3.setIconSize(QSize(110,110))
        self.b3.clicked.connect(self.page)
        self.l3b3 = QVBoxLayout(self.group)
        self.l3b3.addWidget(self.l3)
        self.l3b3.addWidget(self.b3)
        self.l4 = QLabel("                                   PC1 | IP = 192.168.56.1")
        self.b4 = QPushButton()
        self.b4.setIcon(QIcon("pc.png"))
        self.b4.setIconSize(QSize(110,110))
        self.b4.clicked.connect(self.page)
        self.l4b4 = QVBoxLayout(self.group)
        self.l4b4.addWidget(self.l4)
        self.l4b4.addWidget(self.b4)
        self.l5 = QLabel("                                   PC1 | IP = 192.168.56.1")
        self.b5 = QPushButton()
        self.b5.setIcon(QIcon("pc.png"))
        self.b5.setIconSize(QSize(110,110))
        self.b5.clicked.connect(self.page)
        self.l5b5 = QVBoxLayout(self.group)
        self.l5b5.addWidget(self.l5)
        self.l5b5.addWidget(self.b5)
        self.l6 = QLabel("                                   PC1 | IP = 192.168.56.1")
        self.b6 = QPushButton()
        self.b6.setIcon(QIcon("pc.png"))
        self.b6.setIconSize(QSize(110,110))
        self.b6.clicked.connect(self.page)
        self.l6b6 = QVBoxLayout(self.group)
        self.l6b6.addWidget(self.l6)
        self.l6b6.addWidget(self.b6)
        
        self.grid.addLayout(self.l1b1, 0, 0)
        self.grid.addLayout(self.l2b2, 0, 1)
        self.grid.addLayout(self.l3b3, 1, 0)
        self.grid.addLayout(self.l4b4, 1, 1)
        self.grid.addLayout(self.l5b5, 2, 0)
        self.grid.addLayout(self.l6b6, 2, 1)
        self.setCentralWidget(self.group)
    
        
        
        
        self.setCentralWidget(self.group)
        
        
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
 