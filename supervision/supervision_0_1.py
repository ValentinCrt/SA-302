"_version_ = version = 0.1"

!/usr/bin/env python3
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
        self.setWindowIcon(QIcon("logo.png"))
        self.group = QGroupBox()
        self.grid = QGridLayout(self.group)
        
        
        self.boutton1 = QPushButton()
        self.boutton1.setIcon(QIcon("pc.jpg"))
        self.boutton1.setIconSize(QSize(110,110))
        self.boutton1.setText("zz")
        self.grid.addWidget(self.boutton1, 0, 0)
        self.boutton2 = QPushButton()
        self.boutton2.setIcon(QIcon("pc.jpg"))
        self.boutton2.setIconSize(QSize(110,110))
        self.grid.addWidget(self.boutton2, 0, 1)
        
        
        
        
        
        
        
        
        self.setCentralWidget(self.group)
        
        
def main():
    application = QApplication(sys.argv)
    mon_appli = Supervision()
    mon_appli.show()
    sys.exit(application.exec_())


if __name__== '__main__':
    main()