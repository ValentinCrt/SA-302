#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 13:17:15 2022

@author: etudiant
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QGroupBox, QWidget
from PyQt5.QtWidgets import QMenu, QAction, QTextEdit, QMenuBar, QToolBar, QGridLayout, QLineEdit, QMessageBox, QInputDialog
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QSize

class Supervision(QMainWindow):
    
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Supervision")
        self.resize(800,800)
        self.setWindowIcon(QIcon("/logo.jpeg"))
        self.group = QGroupBox()
        self.grid = QGridLayout(self.group)
        
        self.l1 = QLabel("                                   PC1 | IP = 192.168.56.1")
        self.b1 = QPushButton()
        self.b1.setIcon(QIcon("pc.png"))
        self.b1.setIconSize(QSize(110,110))
        self.l1b1 = QVBoxLayout(self.group)
        self.l1b1.addWidget(self.l1)
        self.l1b1.addWidget(self.b1)
        
        self.grid.addLayout(self.l1b1, 0, 0)
        
        self.setCentralWidget(self.group)
           
def main():
    application = QApplication(sys.argv)
    mon_appli = Supervision()
    mon_appli.show()
    sys.exit(application.exec_())


if __name__== '__main__':
    main()
    
