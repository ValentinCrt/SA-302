"""
.. module::int-center
   :platform: Unix
   :synopsis: this module are interfaces, connections and controller together
  
.. moduleauthor:: Duquerroy Léonce <leonce.duquerroy@etu.univ-poitiers.fr>
.. moduleauthor:: Etiembre Baptiste <baptiste.etiembre@etu.univ-poitiers.fr>
.. moduleauthor:: Moreau Mathis <mathis.moreau@etu.univ-poitiers.fr>
"""

import sys
from PyQt5.QtWidgets import QFileDialog, QVBoxLayout, QWidget, QTextEdit, QPushButton, QCheckBox, QApplication
from PyQt5.QtWidgets import QLabel, QTabWidget, QAction, QMainWindow, QToolBar, QGroupBox, QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
import paramiko
import time
sys.path.insert(0, "../connexion/")
from recuperation_MAC_IP import DICO_IP_ETAT

etat = DICO_IP_ETAT

color_a = ""
color_e = "" 

PC = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
IP = ["192.168.89.19","192.168.89.20","192.168.89.21","192.168.89.22","192.168.89.23","192.168.89.24",
      "192.168.89.13","192.168.89.14","192.168.89.15","192.168.89.16","192.168.89.17","192.168.89.18",
      "192.168.89.7","192.168.89.8","192.168.89.9","192.168.89.10","192.168.89.11","192.168.89.12",
      "192.168.89.1","192.168.89.2","192.168.89.3","192.168.89.4","192.168.89.5","192.168.89.6"]

DOC = {"PC1": "192.168.89.19", "PC2": "192.168.89.20", "PC3": "192.168.89.21", "PC4": "192.168.89.22",
       "PC5": "192.168.89.23", "PC6": "192.168.89.24", "PC7": "192.168.89.13", "PC8": "192.168.89.14",
       "PC9": "192.168.89.15", "PC10": "192.168.89.16", "PC11": "192.168.89.17", "PC12": "192.168.89.18",
       "PC13": "192.168.89.7", "PC14": "192.168.89.8", "PC15": "192.168.89.9", "PC16": "192.168.89.10",
       "PC17": "192.168.89.11", "PC18": "192.168.89.12", "PC19": "192.168.89.1", "PC20": "192.168.89.2",
       "PC21": "192.168.89.3", "PC22": "192.168.89.4", "PC23": "192.168.89.5", "PC24": "192.168.89.6",}


class Interface(QMainWindow):
    
    def __init__(self, ip):
        
        assert isinstance(ip, str), "l'ip doit être une chaîne de caractère"
        
        """ this function create the window to send command lines. 
        It also create the menu to use bash files.
        It create a toolbar to add a new tab and close the window
        
        :returns: None
        :rtypes: None
        :raises:
        
        """
        
        
        super().__init__()
        self.text = ip
        separe = self.text.split(" ")
        ip = separe[5]
        self.ip = ip
        self.setWindowTitle("Terminal")
        self.resize(600,600)
        self.menubar = self.menuBar()
        self.baroutils = QToolBar()
        self.onglet = QTabWidget()
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
        
        """ This function creates empty buttons for filling
            
        :returns: self.vide
        :rtypes: PyQt5.QtWidgets.QAction
        :raises: None
        
        """
        self.vide = QAction(QIcon(""),"",self)
        return self.vide

    def open_event(self):
        """ This function adds a shortcut to write a remote bash script.
            
        :returns: None
        :rtypes: None
        :raises: FileNotFoundError
        
        """
        dossier = QFileDialog.getOpenFileName(self)
        fichier = open(dossier[0]).read()
        self.commande.append("cat "+fichier+"> script.sh")

    def add_onglet(self,widget=None,label="Terminal"):
        """
        This function create a block of text to write commande lines and a block of text to retrieve the response from 
        the send command lines.
        It also show the pc status and IP address.
        It create two buttons, one to send to the pc select and the other to several pc.
        
        
        :returns: None
        :rtypes: None
        :raises: 
        
        
        """
        self.group72 = QGroupBox()
        self.grid = QGridLayout()
        self.verticale = QVBoxLayout(self.group72)
        self.fenetre = QVBoxLayout()
        self.IP = QLabel(self.text)
        self.etat = QLabel("off")
        self.widget = QWidget()
        if IP != "":
            self.etat.setText("on")
        self.commande = QTextEdit()
        self.commande.setStyleSheet("color: white; background: rgba(56, 4, 40, 0.9)")
        self.reponse = QTextEdit()
        self.reponse.setStyleSheet("color: white; background: rgba(56, 4, 40, 0.9)")
        self.reponse.setReadOnly(True)
        
        self.envoyers = QPushButton("Envoyers")
        self.envoyers.clicked.connect(self.send)
        self.envoyers.setFixedSize(110,30)
        
        self.envoyer = QPushButton("Envoyer")
        self.envoyer.clicked.connect(lambda: self.sendu(self.ip))
        self.envoyer.setFixedSize(110,30)
        
        self.grid.addWidget(self.etat, 0, 0)
        self.grid.addWidget(self.IP,0,1)
        self.grid.addWidget(self.envoyer,0,2)
        self.grid.addWidget(self.envoyers,0,3)
        
        self.verticale.addLayout(self.grid)
        self.verticale.addWidget(self.commande)
        self.verticale.addWidget(self.reponse)
        self.fenetre.addWidget(self.group72)
        self.widget.setLayout(self.fenetre)
        self.onglets.append(self.widget)
        self.onglet.addTab( self.onglets[-1] , 'Page %s' % len(self.onglets) )
        self.onglet.setCurrentIndex( len(self.onglets)-1 )
        
        
    def send(self):
        """  
        
        :returns: None
        :rtypes: None
        :raises: 
        
        """
        envoyer = Envoyer(self.commande, self.reponse)
        self.windows.append(envoyer)
        envoyer.show()
        
    def sendu(self, host: str):
        
        assert isinstance(host, str), "host doit être une chaîne de caractère"
        
        """ this fonction initializes an ssh connection, sends a command to the target pc  and displays the result of the command.
            
        :returns: None
        :rtypes: None
        :raises: NoValidConnectionsError
        
        """


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
        """
        This function change the pc status and close the window.
        
        :returns: None
        :rtypes: None
        :raises:
        
        
        """
        self.etat.setText("off")
        self.IP.setText("")
        self.close()
        
    def fermer_onglet(self):
        """ Close 
            
        :returns: None
        :rtypes: None
        :raises: None
        
        """
        self.onglet.removeTab()
    
class Supervision(QMainWindow):
    
    
    def __init__(self):
        """
        This function create the window to supervised 24 pc.
        
        :returns: None
        :rtypes: None
        :raises:
        
        """
        super().__init__()
        self.setWindowTitle("Supervision")
        self.resize(800,800)
        self.setWindowIcon(QIcon("images/logo.png"))
        self.group = QGroupBox()
        self.grid = QGridLayout(self.group)
        self.setCentralWidget(self.group)
        self.windows = []
        self.create_bouton()
        
        self.baroutils1 = QToolBar()
        self.change = QAction(QIcon("images/dal.png"), "Daltonien", self)
        self.dechange = QAction(QIcon("images/nondal.png"), "Non-Daltonien", self)
        self.change.setShortcut("Ctrl+D")
        self.dechange.setShortcut("Ctrl+N")
        self.baroutils1.addAction(self.change)
        self.baroutils1.addAction(self.dechange)
        self.change.triggered.connect(self.daltonien)
        self.dechange.triggered.connect(self.nondaltonien)
        self.addToolBar(self.baroutils1)
            
        
    def daltonien(self):
        """
        This function changes the color for color blind people.
        
        :returns: None
        :rtypes: None
        :raises: None
        
        """
        self.Y = 0
        color_a = "#FFD700"
        color_e = "#9932CC"
        for i in range(4):
            for j in range(6):
                Y = IP[self.Y]
                if etat[Y] == False:
                    self.grid.itemAtPosition(i, j).itemAt(1).widget().setStyleSheet("background-color: "+color_e+"")
                    self.grid.itemAtPosition(i, j).itemAt(1).widget().setDisabled(True)
                else:
                    self.grid.itemAtPosition(i, j).itemAt(1).widget().setStyleSheet("background-color: "+color_a+"")
                self.Y+=1
                
    def nondaltonien(self):
        """
        This function put normal colors.
        
        :returns: None
        :rtypes: None
        :raises: None
        
        """
        self.Y = 0
        color_a = "#7CFC00"
        color_e = "#DC143C"
        for i in range(4):
            for j in range(6):
                Y = IP[self.Y]
                if etat[Y] == False:
                    self.grid.itemAtPosition(i, j).itemAt(1).widget().setStyleSheet("background-color: "+color_e+"")
                    self.grid.itemAtPosition(i, j).itemAt(1).widget().setDisabled(True)
                else:
                    self.grid.itemAtPosition(i, j).itemAt(1).widget().setStyleSheet("background-color: "+color_a+"")
                self.Y+=1
    
    
    def create_bouton(self):
        """
        This function create buttons for all pc. It show the name and IP adress of the pc.
        
        :returns: None
        :rtypes: None
        :raises:
        
        """
        self.Y = 0
        color_a = "#7CFC00"
        color_e = "#DC143C"
        for i in range(4):
            for j in range(6):
                self.label = QLabel("PC"+str(PC[self.Y])+"   IP : "+IP[self.Y])
                self.bouton = QPushButton()
                Y = IP[self.Y]
                if etat[Y] == False:
                    self.bouton.setStyleSheet("background-color: "+color_e+"")
                    self.bouton.setDisabled(True)
                else:
                    self.bouton.setStyleSheet("background-color: "+color_a+"")
                    
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
        """
        This function allows you to open the interface to write command lines to the pc selected or several pc.
        
        :returns: None
        :rtypes: None
        :raises:
        
        """
        for i in range(4):
            for j in range(6):
                if self.grid.itemAtPosition(i, j).itemAt(1).widget() == self.bouton.sender():
                   ip = self.grid.itemAtPosition(i, j).itemAt(0).widget().text()
               
        window = Interface(ip)
        self.windows.append(window)
        window.show()
        
        
class Envoyer(QMainWindow):

    def __init__(self, commande, reponse):
        
        """
        This function create a window to select the pc that will receive the command lines.
        It create a button to send the command lines once the selection of pc is finished.
        
        :returns: None
        :rtypes: None
        :raises:
        
        
        """
        super().__init__()
        self.commande = commande
        self.reponse = reponse
        self.setWindowTitle("Envoyer")
        self.resize(450,450)
        self.setWindowIcon(QIcon("images/envoyer.png"))
        self.group = QGroupBox()
        self.grille = QGridLayout(self.group)
        self.bsend = QPushButton(self.group)
        self.bsend.setIcon(QIcon("images/envoyer.png"))
        self.bsend.setIconSize(QSize(30,30))
        self.bsend.setFixedSize(40, 40)
        self.bsend.move(180,400)
        self.bsend.clicked.connect(self.sends)
        Y=0
        for i in range(4):
            for j in range(6):
                self.grille.addWidget(QCheckBox("PC"+str(PC[Y])), i, j)
                Y+=1
        
        self.setCentralWidget(self.group)


        
    def sends(self):
        """
        This function allows you to retrive the name of the pc selected to send the command lines.
        
        :returns: None
        :rtypes: None
        :raises:
        
        """
        for i in range(4):
            for j in range(6):
                if self.grille.itemAtPosition(i, j).widget().isChecked():
                    ok = self.grille.itemAtPosition(i, j).widget().text()
                    self.sendus(DOC[ok], ok) #DOC[PC2]
        self.close()
                        
                
    def sendus(self, ip: str, pc_name: str):
        
        assert isinstance(ip, str), "l'ip doit être une chaîne de caractère"
        assert isinstance(pc_name, str), "pc_name doit être une chaîne de caractère"
            
        """ this fonction initializes an ssh connection, sends a command to the target pc  and displays the result of the command.
            
        :returns: None
        :rtypes: None
        :raises: NoValidConnectionsError
        
        """

        username = "etudiant"
        password = "etudiant"

        session = paramiko.SSHClient()
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        session.connect(hostname=ip, username=username, password=password, port="22")
        
        commande = self.commande.toPlainText()
        stdin, stdout, stderr =session.exec_command(commande)
        time.sleep(.5)
        reponse = ""+username+"@deb11"+pc_name+": \n \n"+str(stdout.read().decode())
        self.reponse.append(reponse)
        
        session.close()
                    

def main():
    application = QApplication(sys.argv)
    mon_appli = Supervision()
    mon_appli.show()
    sys.exit(application.exec_())


if __name__== '__main__':
    main()
    
