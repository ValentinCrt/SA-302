# -*- coding: utf-8 -*-
"""
.. module::ssh
   :platform: Unix
   :synopsis: this module is a functional controller test. Only works on one pc.
  
.. moduleauthor:: Duquerroy Léonce <leonce.duquerroy@etu.univ-poitiers.fr>
"""

import paramiko
import time

""" this code initializes an ssh connection, sends a command to the target pc  and displays the result of the command.
            
:returns: None
:rtypes: None
:raises: NoValidConnectionsError

"""

host = "172.20.35.22"
username = "etudiant"
password = "etudiant"

session = paramiko.SSHClient()
session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
session.connect(hostname=host,
                username=username,
                password=password,
                port="22")

commande = ''

while commande != "exit" :
    commande = input("Entrer une commande : ")
    stdin, stdout, stderr =session.exec_command(commande)
    print("\n")
    time.sleep(.5)
    print(stdout.read().decode())

session.close()