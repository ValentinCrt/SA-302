# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 20:54:53 2022

@author: uplay
"""

import paramiko
from getpass import getpass
import time

host = "d11.lab.rt"
username = "etudiant"
password = getpass("entrer le mot de passe de etudiant : ")

session = paramiko.SSHClient()
session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
session.connect(hostname=host,
                username=username,
                password=password,
                port="22")

stdin, stdout, stderr =session.exec_command(input("Entrer une commande : "))
time.sleep(.5)
print(stdout.read().decode())

session.close()