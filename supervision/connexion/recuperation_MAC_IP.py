# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 14:45:43 2022
@author: etudiant
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
.. module::Recup_MAC_IP
   :platform: Unix
   :synopsis: This module is a data recovery and processing test. Only works on one pc.
  
.. moduleauthor:: Moreau Mathis <mathismoreau@etu.univ-poitiers.fr>
"""
import os

""" 
This code retrieves all Mac addresses
and network IP addresses.
:We return 1 list with all Mac addresses, 1 list with all Ip addresses
and a dictionary with the Ip addresses associated with their Mac address.
:rtype: list, dict
:raises: NoValidConnectionsError
"""
#Using the nmap command to scan network hosts
#cmd = 'nmap 192.168.89.* > nmap.txt'
#os.system(cmd)

#Variables
num = ['0','1','2','3','4','5','6','7','8','9']

liste2 = []

MAC=[]

IP = []

IP_CORR = []

IP_ACC = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24"]

COMPT = 0

mon_dico = {}

MAC2 = ['8C:EC:4B:89:90:4F','8C:EC:4B:89:02:F0','8C:EC:4B:88:91:EC','8C:EC:4B:88:90:52','8C:EC:4B:88:90:58','8C:EC:4B:89:01:AC',
        '8C:EC:4B:88:90:A4','8C:EC:4B:89:7E:A1','8C:EC:4B:88:90:AF','8C:EC:4B:89:7E:6F','8C:EC:4B:89:7E:E3','8C:EC:4B:89:7E:5E',
        '8C:EC:4B:88:90:5C','8C:EC:4B:88:91:DD','8C:EC:4B:88:92:FA','8C:EC:4B:88:91:D9','8C:EC:4B:88:91:EF','8C:EC:4B:88:93:8C',
        '8C:EC:4B:88:92:30','8C:EC:4B:88:91:D1','8C:EC:4B:88:92:34','8C:EC:4B:88:91:CF','8C:EC:4B:88:90:19','8C:EC:4B:88:91:F7']

DICO_IP_ETAT = {"192.168.89.19":"éteint","192.168.89.20":"éteint","192.168.89.21":"éteint","192.168.89.22":"éteint","192.168.89.23":"éteint","192.168.89.24":"éteint",
      "192.168.89.13":"éteint","192.168.89.14":"éteint","192.168.89.15":"éteint","192.168.89.16":"éteint","192.168.89.17":"éteint","192.168.89.18":"éteint",
      "192.168.89.7":"éteint","192.168.89.8":"éteint","192.168.89.9":"éteint","192.168.89.10":"éteint","192.168.89.11":"éteint","192.168.89.12":"éteint",
      "192.168.89.1":"éteint","192.168.89.2":"éteint","192.168.89.3":"éteint","192.168.89.4":"éteint","192.168.89.5":"éteint","192.168.89.6":"éteint"}


#Open nmap file
g = open('nmap.txt','r')

for ligne in g:
    for lettre in ligne:
        liste2.append(lettre)
    
g.close()


#Retrieve all MAC addresses of the file
for i in range(len(liste2)-30):
    if liste2[i] + liste2[i+1] + liste2[i+2] + liste2[i+3] + liste2[i+4] + liste2[i+5] + liste2[i+6] + liste2[i+7]+ liste2[i+8]+ liste2[i+9]+ liste2[i+10] + liste2[i+11] == 'MAC Address:':
        if liste2[i+13] + liste2[i+14]+liste2[i+15] + liste2[i+16] + liste2[i+17] + liste2[i+18] + liste2[i+19] + liste2[i+20] + liste2[i+21]+ liste2[i+22]+ liste2[i+23]+ liste2[i+24]+ liste2[i+25]+ liste2[i+26]+ liste2[i+27]+ liste2[i+28]+ liste2[i+29] in MAC2 :
            MAC.append(liste2[i+13] + liste2[i+14]+liste2[i+15] + liste2[i+16] + liste2[i+17] + liste2[i+18] + liste2[i+19] + liste2[i+20] + liste2[i+21]+ liste2[i+22]+ liste2[i+23]+ liste2[i+24]+ liste2[i+25]+ liste2[i+26]+ liste2[i+27]+ liste2[i+28]+ liste2[i+29])
    

#Retrieve all IP addresses of the file
for i in range(len(liste2)-10):
    if liste2[i] + liste2[i+1] + liste2[i+2] == "for":
        if liste2[i+16] and liste2[i+17] in num:
            IP.append(liste2[i+4] + liste2[i+5] + liste2[i+6]+liste2[i+7] + liste2[i+8] + liste2[i+9]+liste2[i+10] + liste2[i+11] + liste2[i+12]+liste2[i+13] + liste2[i+14] + liste2[i+15] + liste2[i+16] + liste2[i+17])
        else :
            if liste2[i+16] in num: 
                IP.append(liste2[i+4] + liste2[i+5] + liste2[i+6]+liste2[i+7] + liste2[i+8] + liste2[i+9]+liste2[i+10] + liste2[i+11] + liste2[i+12]+liste2[i+13] + liste2[i+14] + liste2[i+15] + liste2[i+16])
            else :
                IP.append(liste2[i+4] + liste2[i+5] + liste2[i+6]+liste2[i+7] + liste2[i+8] + liste2[i+9]+liste2[i+10] + liste2[i+11] + liste2[i+12]+liste2[i+13] + liste2[i+14] + liste2[i+15])

for i in IP:
    if i[-2] == '.':
        IP_CORR.append(i)
    else :
        if i[-2] + i[-1] in IP_ACC:
            IP_CORR.append(i)
        else:
            pass
        

#Assigning a key with a MAC address with the value which is the IP address
for i in range(len(MAC)):
    mon_dico[MAC[i]] = IP[i]

for i in DICO_IP_ETAT:
    if i in IP_CORR:
        DICO_IP_ETAT[i] = "Allumé"
        
    

print(mon_dico)
print(MAC)
print(IP_CORR)
print(DICO_IP_ETAT)
