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


#Using the nmap command to scan network hosts
#cmd = 'nmap 192.168.89.* > nmap.txt'
#os.system(cmd)
#cmd1 = 'cp nmap.txt ../interfaces/nmap.txt'
#os.system(cmd1)



#Variables
NUM = ['0','1','2','3','4','5','6','7','8','9']

liste2 = []

MAC=[]

IP = []

IP_V2 = []

IP_ACC = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24"]

COMPT = 0

MON_DICO = {}

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



def Mac(list2, list_mac):
    
    
    """ 
    
    This code retrieves all Mac addresses of the file.
    :returns: MAC
    :rtypes: list
    :raises: 
        
    """
    
    
    assert isinstance(list2, list), "list2 doit être une liste"
    assert isinstance(list_mac, list), "list_mac doit être une liste"
    
    
    for i in range(len(liste2)-30):
        if liste2[i] + liste2[i+1] + liste2[i+2] + liste2[i+3] + liste2[i+4] + liste2[i+5] + liste2[i+6] + liste2[i+7]+ liste2[i+8]+ liste2[i+9]+ liste2[i+10] + liste2[i+11] == 'MAC Address:':
            if liste2[i+13] + liste2[i+14]+liste2[i+15] + liste2[i+16] + liste2[i+17] + liste2[i+18] + liste2[i+19] + liste2[i+20] + liste2[i+21]+ liste2[i+22]+ liste2[i+23]+ liste2[i+24]+ liste2[i+25]+ liste2[i+26]+ liste2[i+27]+ liste2[i+28]+ liste2[i+29] in MAC2 :
                liste2.append(liste2[i+13] + liste2[i+14]+liste2[i+15] + liste2[i+16] + liste2[i+17] + liste2[i+18] + liste2[i+19] + liste2[i+20] + liste2[i+21]+ liste2[i+22]+ liste2[i+23]+ liste2[i+24]+ liste2[i+25]+ liste2[i+26]+ liste2[i+27]+ liste2[i+28]+ liste2[i+29])

#   print(list_mac)
    return list_mac
    


def Ip(list_de_lettre, list_ip, list_ip_version2, numero):
    
    
    """ 
    
    This code retrieves all IP addresses of the file.
    :returns: list_ip, list_ip_version2
    :rtypes: list, list
    :raises:
        
    """
    
    
    assert isinstance(list_de_lettre, list), "list_de_lettre doit être une liste"
    assert isinstance(list_ip, list), "list_ip doit être une liste"
    assert isinstance(list_ip_version2, list), "list_ip_version2 doit être une liste"
    assert isinstance(numero, list), "numero doit être une liste"
    
    
    for i in range(len(liste2)-10):
        if liste2[i] + liste2[i+1] + liste2[i+2] == "for":
            if liste2[i+16] and liste2[i+17] in numero:
                IP.append(liste2[i+4] + liste2[i+5] + liste2[i+6]+liste2[i+7] + liste2[i+8] + liste2[i+9]+liste2[i+10] + liste2[i+11] + liste2[i+12]+liste2[i+13] + liste2[i+14] + liste2[i+15] + liste2[i+16] + liste2[i+17])
            else :
                if liste2[i+16] in numero: 
                    IP.append(liste2[i+4] + liste2[i+5] + liste2[i+6]+liste2[i+7] + liste2[i+8] + liste2[i+9]+liste2[i+10] + liste2[i+11] + liste2[i+12]+liste2[i+13] + liste2[i+14] + liste2[i+15] + liste2[i+16])
                else :
                    IP.append(liste2[i+4] + liste2[i+5] + liste2[i+6]+liste2[i+7] + liste2[i+8] + liste2[i+9]+liste2[i+10] + liste2[i+11] + liste2[i+12]+liste2[i+13] + liste2[i+14] + liste2[i+15])

    for i in list_ip:
        if i[-2] == '.':
            list_ip_version2.append(i)
        else :
            if i[-2] + i[-1] in IP_ACC:
                list_ip_version2.append(i)
            else:
                pass
       
#   print(list_ip)
#   print(list_ip_version2)
    return list_ip, list_ip_version2    



def Mac_Ip(list_mac, list_ip, dico_mac_ip):
    
    
    """ 
    
    This code Assignes a key with a MAC address with the value which is the IP address.
    :returns: dico_mac_ip
    :rtypes: dict
    :raises:
        
    """
    
    
    assert isinstance(list_mac, list), "list_mac doit être une liste"
    assert isinstance(list_ip, list), "list_ip doit être une liste"
    assert isinstance(dico_mac_ip, dict), "dico_mac_ip doit être un dictionnaire"
    
    
    for i in range(len(list_mac)):
        dico_mac_ip[list_mac[i]] = list_ip[i]
    
#   print(dico_mac_ip)
    return dico_mac_ip



def Ip_Etat(dico_ip_etat, list_ip_version2):
    
    
    """ 
    
    This code Associates the IP addresses of computers with their current states.
    :returns: dico_ip_etat
    :rtypes: dict
    :raises:
        
    """
    
    
    assert isinstance(dico_ip_etat, dict), "dico_ip_etat doit être un dictionnaire"
    assert isinstance(list_ip_version2, list), "list_ip_version2 doit être une liste"
    
    
    for i in dico_ip_etat:
       if i in list_ip_version2:
           dico_ip_etat[i] = "allumé"
           
#   print(dico_ip_etat)
    return dico_ip_etat
        


#Launch of modules  
  
Mac(liste2, MAC)
Ip(liste2, IP, IP_V2, NUM)
Mac_Ip(MAC, IP, MON_DICO)
Ip_Etat(DICO_IP_ETAT, IP_V2)
