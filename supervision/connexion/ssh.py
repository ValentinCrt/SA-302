# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 20:54:53 2022

@author: uplay
"""

import paramiko

client = paramiko.SSHClient()                                   # ouverture d'une session
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())    # clée ssh ?
client.connect('@IP', username='etudiant', password='etudiant') # connexion au pc
stdin, stdout, stderr = client.exec_command("mkdir test")       # commande de test
stdin, stdout, stderr = client.exec_command("ls")               # vérification de la commande de test
for line in stdout.read().splitlines():                         # écriture des commande du dessus
    print (line)