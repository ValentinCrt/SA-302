.. Saé-302 documentation master file, created by
   sphinx-quickstart on Mon Dec  5 09:18:10 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Saé-302's documentation!
===================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Introduction
==================
Notre projet est de créer une application graphique PyQt de gestion d’une salle de TP informatique. 

Nous disposions aux préalables des machines virtuelles pour effectuer les différents tests. Par la suite, l’application développée doit pouvoir fonctionner dans la salle 1. 

L’objectif principale voulu est de pouvoir envoyer un script sur plusieurs ordinateurs et de pouvoir avoir les réponses de chaque ordinateur. Nous saurons les différentes réponses des ordinateurs.

Contexte
==================
Pour effectuer notre projet, nous avons donc eu des machines virtuelles où une des machines était une version Ubuntu graphique. Grâce à cela nous avons pu reproduire une topologie d’une entreprise où le poste Administrateur voulait la supervision et le contrôle de différents postes d’employées. 

Pour rendre notre projet plus réaliste nous avons eu accès à la salle 1. Nous avons réussi à effectuer un plan d'adressage physique que vous pouvez voir ci-dessous.

Pour développer cette application, nous dévions utiliser l’outil de programmation python que nous connaissons bien grâce aux multiples cours que nous avons eu.
Nous savions aussi grâce à nos cours de réseaux que nous aurons aussi besoin de paquet NMAP pour localiser le réseau dont nous bénéficions. Par la suite nous avons appris à utiliser l’outil paramiko.


Méthodologie
==================

Pour commencer à développer, nous avons commencé à coder l'application en la divisant en trois parties. 

Une partie Interface où nous avons coder l’interface graphique où nous trouvons les différents ordinateurs alumer et des boutons qui fait une animation ou nous pouvons écrire votre commande ou notre script que nous pouvons envoyer à plusieurs postes.
Dans le deuxième cadre vous recevrez les résultats des différents postes de manière compréhensible   

Une deuxième partie qui s’intéresse à la partie connexion. Ici nous avons créé des scripts python pour la récupération des adresses physiques.Grâce au retour du script qui utilise le paquet NMAP, nous pouvons envoyer la liste des postes allumés à l'interface qui réagira en conséquence.

Une troisième partie qui s'intéresse à la partie contrôleur. Dans cette partie, nous avons développé essentiellement la partie envoie et réception des commandes. Nous utilisons ici la correspondance entre les adresses logiques et les adresses physiques.

Nous avons donc utilisé l’outil de programmation python avec la documentation Pyqt qui permet la programmation événementielle. Nous avons aussi utilisé le paquet NMAP qui s’installe avec un compte Administrateur.

Daltonisme
==================
Le daltonisme est une anomalie de la vision affectant la perception des couleurs. Le daltonisme est généralement provoqué par un trouble fonctionnel d’un ou de plusieurs cônes de la rétine. La gravité du daltonisme peut varier en fonction de la personne, et vous pourriez ne pas remarquer en souffrir sans avoir fait l’objet d’un test de la vue et de la perception des couleurs.

Les daltonismes « rouges-verts » sont les plus courants et même souvent considérés comme « le » seul daltonisme. Cela s’explique par le fait qu’ils sont transmis par le chromosome X de la mère et que le gène est récessif.

Source : Les_yeux_du_datonisme.fr

Tutoriel 
==================

Installer Spyder pour pouvoir par la suite lancer le programme.
Instaler Pyp Paramiko. 
Installer Python3.
Effectuer un git clone le projet.
Lancer le programme.


Conclusion du projet
==================

Nous avons réussi à faire notre application comme nous le souhaitons, cela est donc une réussite pour le groupe. Nous avons l'intégralité des fonctionnalités demandées ainsi que des supplémentaires. La seule difficulté rencontrée cela a été de comprendre le fonctionnement du module Paramiko. Le point positif du projet cela a été que nous avons totalement réussi sans aucun problème à travailler en groupe et nous avons réussi à prendre des moment pour que a quatre nous prenions du recul et que nous réfléchissions à la meilleure solution pour notre application.

Adresse Github :
https://github.com/valcrrn/SA-302.git
gh repo clone valcrrn/SA-302

Bilan personnel : 

Léonce : Ce projet m’a permis de pouvoir apprendre un nouveau module Paramiko qui je pense me sera très utile pour la suite de mes études. 

Mathis : Ce projet m’a permis de pouvoir apprendre à coder a plusieurs sur le même programme et à pouvoir présenter ma solution a des collaborateurs.

Baptiste : Ce projet m'a permis de pouvoir apprendre à coder d’une manière plus propre pour une meilleure compréhension pour une personne tiers. 

Valentin  : Ce projet m’a permis de pouvoir apprendre à respecter un planning et surtout commenter le travail que je produisais. 
Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
* :ref:`module`

