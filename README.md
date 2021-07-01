# Delete-temporary-folders-and-filses_Windows&Linix 

Ce script permet de supprimer régulièrement les dossiers et les fichiers temporaires sous Windows et Linux 

  

#Compatibilité 

Testé sous Windows 10, Centos8. 
 


#Prérequis 

Installation du module Paramiko : 

 pip install paramiko 

Accès SSH pour vous connecter sur les machines distantes. 




#Lancement 

Windows : 

   Python script1.py 
 
Linux : 

  Python3 script1.py 

 
 


#Exemple de fonctionnement


![image](https://user-images.githubusercontent.com/85261915/122476130-00461800-cfc6-11eb-929e-39d7c596e0e1.png)






#Construction 

Deux scripts python : 

Le premier “script1”, permet de : 

   Afficher les machines disponibles sur une plage d’adresses donnée avec le nom et l’adresse IP.  

   Entrer l’adresse IP de la machine sur laquelle vous souhaitez supprimer les fichiers/dossiers temporaires. 

   Se connecter en SSH sur la machine distante. 

   Copier le deuxième script “script2” sur la machine distante. 

   Exécuter le “script2” sur la machine distante. 

 

Le deuxième “script2”, permet de :

   Calculer l’âge des dossiers/fichiers temporaires et le comparer avec la durée maximale indiquée "days".
   
   Afficher le contenu du répertoire "temp" (sous Windows), ou "tmp" (sous linux), les dossiers/fichiers dont l'âge est supperieur ou égale à "days", seront affichés en rouge.
   
   Supprimer les dossiers/fichiers dont l’âge est supérieur ou égale à days". 
   
   Afficher le contenu du répertoire "temp" (sous Windows), ou "tmp" (sous linux) après la suppression.

