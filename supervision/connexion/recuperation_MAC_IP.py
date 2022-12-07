# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 14:45:43 2022

@author: etudiant
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""
import os

""" 
This code retrieves all Mac addresses
and network IP addresses.

:We return 1 list with all Mac addresses, 1 list with all Ip addresses
and a dictionary with the Ip addresses associated with their Mac address.

:rtype: list, dict
"""
#Using the nmap command to scan network hosts
cmd = 'echo etudiant | sudo -S nmap 172.20.90.* > nmap.txt'
os.system(cmd)

#Variables
liste2 = []
MAC=[]
IP = []
mon_dico = {}
MAC2 = ['8C:EC:4B:89:90:4F','8C:EC:4B:89:02:F0','8C:ER:4B:88:91:EC','8C:ER:4B:88:90:52','8C:ER:4B:88:90:52','8C:ER:4B:89:01:AC',
        '8C:ER:4B:88:90:A4','8C:ER:4B:89:7E:A1','8C:ER:4B:88:90:AF','8C:ER:4B:89:7E:6F','8C:ER:4B:89:7E:E3','8C:ER:4B:89:7E:5E',
        '8C:ER:4B:88:90:5C','8C:ER:4B:88:91:DD','8C:ER:4B:88:92:FA','8C:ER:4B:88:91:D9','8C:ER:4B:88:91:EF','8C:ER:4B:88:93:8C',
        '8C:ER:4B:88:92:30','8C:ER:4B:88:91:D1','8C:ER:4B:88:92:34','8C:ER:4B:88:91:CF','8C:ER:4B:88:90:19','8C:ER:4B:88:91:F7']
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
        IP.append(liste2[i+4] + liste2[i+5] + liste2[i+6]+liste2[i+7] + liste2[i+8] + liste2[i+9]+liste2[i+10] + liste2[i+11] + liste2[i+12]+liste2[i+13] + liste2[i+14] + liste2[i+15])

#Assigning a key with a MAC address with the value which is the IP address
for i in range(len(MAC)):
    mon_dico[MAC[i]] = IP[i]

print(mon_dico)
