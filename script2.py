

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




# initiqliwing the count
deleted_folders_count = 0
deleted_files_count = 0

##specify the days
days = 1
# converting days to seconds
seconds = days * 24 * 60 * 60
# dictionary init
dict_file_folder ={}


# platform.system() returns the system/OS name
platforme = platform.system()
if platforme == "Windows":
    username = getpass.getuser()
    #path of temporary files
    path = 'C:/Users/' + username + '/AppData/Local/Temp'
else:
    #path
    path = '/tmp'
# check if the path exits 
if os.path.exists(path):
    for files in os.listdir(path):
        #path of the folder/file
        path1 = os.path.join(path, files)
        name = basename(path1)
        
        #getting ctime of the folder/file
        st=os.stat(path1)
        #retuns current time in seconds
        resul = (time.time()-st.st_mtime)
        age = resul / 86400
        dict_file_folder.update({name:age})
               

    # if statement evaluate empty dictionary
    if bool(dict_file_folder) is False:
            print("le répertoire temp est vide")
            exit()
    # else statement print table from dictionary        
    #comparing with the days
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
            #path of the folder/file
            path1 = os.path.join(path, files)
                
            #getting ctime of the folder/file
            st=os.stat(path1)
            #retuns current time in seconds
            resul = (time.time()-st.st_mtime)
    
            #comparing with the days
            if resul >= seconds:
                try:
                    #removing the folders
                    shutil.rmtree(path1)
                    deleted_folders_count += 1 # incrementing count
                except OSError:
                    #removing the files
                    os.remove(path1)
                    deleted_files_count += 1 # incrementing countt
                        
                        
              
            else:
                        
                pass
    print(f"Total folders deleted: {deleted_folders_count}")
    print(f"Total files deleted: {deleted_files_count}")
    

                             
                           
else:
    # file/folder is not found
    print(f'"{path}" n\'existe pas, verifier le chemin')

dict2_file_folder = {}
# check if the path exits 
if os.path.exists(path):
    for files in os.listdir(path):
        #path of the folder/file
        path1 = os.path.join(path, files)
        name = basename(path1)
        
        #getting ctime of the folder/file
        st=os.stat(path1)
        #retuns current time in seconds
        resul = (time.time()-st.st_mtime)
        age = resul / 86400
        dict2_file_folder.update({name:age})
               

    # if statement evaluate empty dictionary
    if bool(dict2_file_folder) is False:
            print("le répertoire temp est vide")
            exit()
    # else statement print table from dictionary        
    #comparing with the days
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
    # file/folder is not found
    print(f'"{path}" n\'existe pas, verifier le chemin')

    

