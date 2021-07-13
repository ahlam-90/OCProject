
import socket
import os
import re
import subprocess
import time
import paramiko
import stat
import sys




#la requête ping 
ping1 = "ping -n 1 "

# initialisation du dictionnaire
dict_IP_Online ={}
# boucle ping à travers la plage d'adresses IP
for ping in range(1,6):
    address = "192.168.0." + str(ping)
    comm = ping1 + address
    response = subprocess.Popen(comm, shell=True, stdout=subprocess.PIPE).communicate()[0]
            

    # dictionnaire mis à jour avec le nom et l'adresse IP des machines accessibles
    # la chaine 'TTL=', reponse utilisée pour le système windows
    if 'TTL=' in str(response):
            #le  bloc 'try" socket.gethostbyaddr() sur l'adresse IP
        
            try:
                    hostname = socket.gethostbyaddr(address)
            # le bloc except  en cas d'erreur
            except socket.herror:
                    hostname = ("Unknown",)
            dict_IP_Online.update({hostname[0]:address})
            
            
    #  la chaine 'ttl=', reponse utilisée pour le système Unix 
    elif 'ttl=' in str(response):
            #le  bloc 'try" socket.gethostbyaddr() sur l'adresse IP       
            try:
                    hostname = socket.gethostbyaddr(address)
            except socket.herror:
                    hostname = ("Unknown",)
            dict_IP_Online.update({hostname[0]:address})



# l'instruction "if" évalue un dictionnaire vide
if bool(dict_IP_Online) is False:
        print("All IP are offline or unreachable")
        exit()
# instruction "else" imprime un tableau à partir du dictionnaire       
else:
       equal = '=' * 40
       dash = '-' * 40
       print(equal)
       print("{: ^1}{: ^18}{: ^2}{: ^1}".format("|","hostname","||", "IP","|"))
       print(equal)
       for key, value in dict_IP_Online.items():
               print("{: ^1}{: ^18}{: ^2}{: ^1}".format("|",key,"||", value,"|"))
               print(dash)



#La connexion ssh
# la boucle "while" exécute l'entrée tant que l'ip entrée n'est pas une valeur du dictionnaire
hostip = input("Enter IP address from the list to initiate the SSH connection ? (x to exit) ")
while hostip not in dict_IP_Online.values():
        if hostip == "x":
                exit()
        else:
                hostip = input("Please enter IP address from the list to initiate the SSH connection? (x to exit) ")


username = input("Enter the SSH login ?")                        
password = input("Enter the SSH password ?")
username2 = input("Enter the username for the local server: ")



# le bloc "try" ssh se connecte avec le module paramiko
try:
    # create a new SSHClient
    ssh = paramiko.SSHClient()
    
    # paramiko.AutoAddPolicy() pour autoriser la connexion SSH vers un serveur distant avec des clés SSH inconnues
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # connecter le client à l'hôte distant avec le nom d'utilisateur et le mot de passe des informations d'identification
    ssh.connect(hostip, username=username, password=password)
    
    # exécuter la commande sur l'hôte distant et renvoyer un tuple contenant le stdin, le stdout et le stderr de l'hôte
    # command get OS system version
    # La commande pour obtenir la version du système d'exploitation
    cmd = 'wmic os get Caption | findstr /v Caption'
    stdin, stdout, stderr = ssh.exec_command(cmd)
    resu = stdout.read()
    
    # instruction if sur la chaîne 'Windows' stdout
    
    if 'Windows' in str(resu):
        
        # transferts de fichiers gérés par open_sftp() sur l'instance ssh de Paramiko.SSHClient
        sftp = ssh.open_sftp()
        #Copiez le deuxième script sur le serveur distant
        sftp.put("C:\\Users\\" + username2 + "\\Desktop\\script2.py", "C:\\Users\\" + username + "\\Desktop\\script2.py")
        #fermer la connexion ssh
        sftp.close()
        #exécuter le deuxième script sur le serveur distant
        stdout = ssh.exec_command('python C:\\Users\\' + username + '\\Desktop\\script2.py')[1]
        stdout = stdout.read().decode('utf-8')
        #Afficher les résultats du script
        print(stdout)
        
    else:
        username3 = input("Entrer le nom d'utilisateur admin: ")
        sftp = ssh.open_sftp()
        sftp.put("C:\\Users\\" + username2 + "\\Desktop\\script2.py", "/home/" + username3 + "/Desktop/script2.py")
        sftp.close()
        stdout = ssh.exec_command('python3 /home/' + username3 + '/Desktop/script2.py')[1]
        for line in stdout:
            print(line)
            ssh.close()
        sys.exit(0)
        
        
        

# le bloc except en cas de problème d'authentification et passer la boucle
except paramiko.ssh_exception.NoValidConnectionsError as error:
    print(error)
  
