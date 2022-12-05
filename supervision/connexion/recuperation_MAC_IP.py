# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os

#Using the nmap command to scan network hosts
cmd = 'echo etudiant | sudo -S nmap 172.20.90.* > nmap.txt'
os.system(cmd)

#Variables
liste2 = []
MAC=[]
IP = []
mon_dico = {}

#Open nmap file
g = open('nmap.txt','r')

for ligne in g:
    for lettre in ligne:
        liste2.append(lettre)
    
g.close()

#Retrieve all MAC addresses of the file
for i in range(len(liste2)-30):
    if liste2[i] + liste2[i+1] + liste2[i+2] + liste2[i+3] + liste2[i+4] + liste2[i+5] + liste2[i+6] + liste2[i+7]+ liste2[i+8]+ liste2[i+9]+ liste2[i+10] + liste2[i+11] == 'MAC Address:':
        MAC.append(liste2[i+13] + liste2[i+14]+liste2[i+15] + liste2[i+16] + liste2[i+17] + liste2[i+18] + liste2[i+19] + liste2[i+20] + liste2[i+21]+ liste2[i+22]+ liste2[i+23]+ liste2[i+24]+ liste2[i+25]+ liste2[i+26]+ liste2[i+27]+ liste2[i+28]+ liste2[i+29])

#Retrieve all IP addresses of the file
for i in range(len(liste2)-10):
    if liste2[i] + liste2[i+1] + liste2[i+2] == "for":
        IP.append(liste2[i+4] + liste2[i+5] + liste2[i+6]+liste2[i+7] + liste2[i+8] + liste2[i+9]+liste2[i+10] + liste2[i+11] + liste2[i+12]+liste2[i+13] + liste2[i+14] + liste2[i+15])

#Assigning a key with a MAC address with the value which is the IP address
for i in range(len(MAC)):
    mon_dico[MAC[i]] = IP[i]

print(mon_dico)
