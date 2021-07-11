

import socket
import os
import re
import subprocess
import platform
import time
import paramiko
import shutil
import stat
import getpass
from os.path import basename




# initialiser le compte
deleted_folders_count = 0
deleted_files_count = 0

# préciser le nombre de jours
days = 1
# convertir les jours en secondes
seconds = days * 24 * 60 * 60
# initialisation du dictionnaire
dict_file_folder ={}


# platform.system() renvoie le nom du système/système d'exploitation
platforme = platform.system()
if platforme == "Windows":
    username = getpass.getuser()
    #chemin des fichiers temporaires
    path = 'C:/Users/' + username + '/AppData/Local/Temp'
else:
    #chemin
    path = '/tmp'
# vérifier si le chemin existe 
if os.path.exists(path):
    for files in os.listdir(path):
        #chemin du dossier/fichier
        path1 = os.path.join(path, files)
        name = basename(path1)
        
        #obtenir le ctime du dossier/fichier
        st=os.stat(path1)
        #renvoie l'âge du dossier/fichier en secondes
        resul = (time.time()-st.st_mtime)
        # Convertir le résultat en jours
        age = resul / 86400
        # mettre à jour le dictionnaire
        dict_file_folder.update({name:age})
               

    # l'instruction "if" évalue un dictionnaire vide
    if bool(dict_file_folder) is False:
            print("le répertoire temp est vide")
            exit()
    # instruction "else" imprime un tableau à partir du dictionnaire        
    
    else:
        
        print("voici le contenu du répertoire temp avec l\'age de chaque dossier/fichier avant la supprisssion: ") 
        equal = '=' * 80
        dash = '-' * 80
        print(equal)
        print("{: ^1}{: ^18}{: ^2}{: ^1}".format("|","name","||", "age","|"))
        print(equal)

        for key, value in dict_file_folder.items():
                    print("{: ^1}{: ^18}{: ^2}{: ^1}".format("|",key, "||", value,"|"))
                    print(dash)
    
                  
        
    for files in os.listdir(path):
            #chemin du dossier/fichier
            path1 = os.path.join(path, files)
                
            #obtenir le ctime du dossier/fichier
            st=os.stat(path1)
            #obtenir le ctime du dossier/fichier
            resul = (time.time()-st.st_mtime)
    
            #comparer avec "days"
            if resul >= seconds:
                try:
                    #suppression des dossiers
                    shutil.rmtree(path1)
                    deleted_folders_count += 1 # incrémentation du nombre
                except OSError:
                    #suppression des fichiers
                    os.remove(path1)
                    deleted_files_count += 1 # incrémentation du nombre
                        
                        
              
            else:
                        
                pass
    print(f"Total folders deleted: {deleted_folders_count}")
    print(f"Total files deleted: {deleted_files_count}")
    

                             
                           
else:
    # fichier/dossier introuvable
    print(f'"{path}" n\'existe pas, verifier le chemin')

dict2_file_folder = {}
#Vérifier si le chemin existe
if os.path.exists(path):
    for files in os.listdir(path):
        #chemin du dossier/fichier
        path1 = os.path.join(path, files)
        name = basename(path1)
        
        #obtenir le ctime du dossier/fichier
        st=os.stat(path1)
        #obtenir le ctime du dossier/fichier
        resul = (time.time()-st.st_mtime)
        age = resul / 86400
        dict2_file_folder.update({name:age})
               

    # l'instruction "if" évalue un dictionnaire vide
    if bool(dict2_file_folder) is False:
            print("le répertoire temp est vide")
            exit()
    # instruction "else" imprime un tableau à partir du dictionnaire        
    #Comparer avec "days"
    else:
        
        print("voici le contenu du répertoire temp avec l\'age de chaque dossier/fichier après la supprisssion: ") 
        equal = '=' * 80
        dash = '-' * 80
        print(equal)
        print("{: ^1}{: ^18}{: ^2}{: ^1}".format("|","name","||", "age","|"))
        print(equal)
        
        for key, value in dict2_file_folder.items():
                    print("{: ^1}{: ^18}{: ^2}{: ^1}".format("|",key, "||", value,"|"))
                    print(dash)

    
else:
    # Ficher/Dossier introuvable
    print(f'"{path}" n\'existe pas, verifier le chemin')

    

