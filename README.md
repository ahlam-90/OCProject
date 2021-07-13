# Delete-temporary-folders-and-filses_Windows&Linux 

Ce script permet de supprimer régulièrement les dossiers et les fichiers temporaires sous Windows et Linux 

  

## Compatibilité 

Testé sous Windows 10, Centos8. 
 



## Prérequis 

Installation du module Paramiko : pip install paramiko


Accès SSH pour vous connecter sur les machines distantes. 





## Lancement 

Windows : 

   Python script1.py 
 
Linux : 

  Python3 script1.py 

 
 



## Construction 

Deux scripts python : 

### Le premier “script1”permet de:

   Afficher les machines disponibles sur une plage d’adresses donnée avec le nom et l’adresse IP.  

   Entrer l’adresse IP de la machine sur laquelle vous souhaitez supprimer les fichiers/dossiers temporaires. 

   Se connecter en SSH sur la machine distante. 

   Copier le deuxième script “script2” sur la machine distante. 

   Exécuter le “script2” sur la machine distante. 

 

### Le deuxième “script2”, permet de :

   Calculer l’âge des dossiers/fichiers temporaires et le comparer avec la durée maximale indiquée "days".
   
   Afficher le contenu du répertoire "temp" (sous Windows), ou "tmp" (sous linux).
   
   Supprimer les dossiers/fichiers dont l’âge est supérieur ou égale à days". 
   
   Afficher le contenu du répertoire "temp" (sous Windows), ou "tmp" (sous linux) après la suppression.
   
   
   
   
   
   
   
   
 ## Exemple de fonctionnement: 
 Test avec days=1jour(les dossiers/fichiers dont l'âge >= 1jour seront supprimés)


![image](https://user-images.githubusercontent.com/85261915/124932879-b8824180-e003-11eb-9a3d-ebf735388775.png)
![image](https://user-images.githubusercontent.com/85261915/124932930-c33cd680-e003-11eb-80d1-216910f675bb.png)
![image](https://user-images.githubusercontent.com/85261915/124932983-ccc63e80-e003-11eb-846f-aefc26b2ceab.png)

