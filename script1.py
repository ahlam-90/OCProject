
import socket
import os
import platform
import re
import subprocess
import time
import paramiko
import stat
import sys




# ping request construction according to the system/OS on which the program is being currently executed 
# platform.system() returns the system/OS name
osplatform = platform.system()
if (osplatform == "Windows"):
        ping1 = "ping -n 1 "
else:
        ping1 = "ping -c 1 "


# dictionary init
dict_IP_Online ={}
# ping loop through the IP address range
for ping in range(1,6):
    address = "192.168.0." + str(ping)
    comm = ping1 + address
    response = subprocess.Popen(comm, shell=True, stdout=subprocess.PIPE).communicate()[0]
            

    # dictionary updated with the hostname and ip address of the reachable machines
    # socket.gethostbyaddr() returns a tuple containing hostname, alias list and IP address of the host 
    # if statement on string 'TTL=' response used for Windows system
    if 'TTL=' in str(response):
            # the try block process socket.gethostbyaddr() on ip address
            try:
                    hostname = socket.gethostbyaddr(address)
            # the except block process in case of the error.
            except socket.herror:
                    hostname = ("Unknown",)
            dict_IP_Online.update({hostname[0]:address})
            
            
    # if statement on string 'ttl=' response used for Unix system
    elif 'ttl=' in str(response):
            # the try block process socket.gethostbyaddr() on ip address       
            try:
                    hostname = socket.gethostbyaddr(address)
            except socket.herror:
                    hostname = ("Unknown",)
            dict_IP_Online.update({hostname[0]:address})



# if statement evaluate empty dictionary
if bool(dict_IP_Online) is False:
        print("All IP are offline or unreachable")
        exit()
# else statement print table from dictionary        
else:
       equal = '=' * 40
       dash = '-' * 40
       print(equal)
       print("{: ^1}{: ^18}{: ^2}{: ^1}".format("|","hostname","||", "IP","|"))
       print(equal)
       for key, value in dict_IP_Online.items():
               print("{: ^1}{: ^18}{: ^2}{: ^1}".format("|",key,"||", value,"|"))
               print(dash)



# while loop execute input as long as ip entered is not in dictionary value
hostip = input("Enter IP address from the list to initiate the SSH connection ? (x to exit) ")
while hostip not in dict_IP_Online.values():
        if hostip == "x":
                exit()
        else:
                hostip = input("Please enter IP address from the list to initiate the SSH connection? (x to exit) ")


username = input("Enter the SSH login ?")                        
password = input("Enter the SSH password ?")
username2 = input("Enter the username for the local server: ")


# the try block process ssh connect with paramiko module
try:
    # create a new SSHClient
    ssh = paramiko.SSHClient()
    # policy as paramiko.AutoAddPolicy() to allow the Python script to SSH to a remote server with unknown SSH keys
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # connect the client to the host with the credentials username and password
    ssh.connect(hostip, username=username, password=password)
    # execute the command on the remote host and return a tuple containing the stdin, stdout, and stderr from the host
    # command get OS system version
    cmd = 'wmic os get Caption | findstr /v Caption'
    stdin, stdout, stderr = ssh.exec_command(cmd)
    resu = stdout.read()
    # if statement on string 'Windows' stdout
    
    if 'Windows' in str(resu):
        #file transfers handled by open_sftp() on ssh instance of Paramiko.SSHClient
        sftp = ssh.open_sftp()
        #Copy the second script to the remote server
        sftp.put("C:\\Users\\" + username2 + "\\Desktop\\script2.py", "C:\\Users\\" + username + "\\Desktop\\script2.py")
        #close ssh connection
        sftp.close()
        #run the second script on the remote server
        stdout = ssh.exec_command('python C:\\Users\\' + username + '\\Desktop\\script2.py')[1]
        stdout = stdout.read().decode('utf-8')
        #View script results
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
        
        
        
# the except block process in case on authentification issues and pass the loop              
except paramiko.ssh_exception.NoValidConnectionsError as error:
    print(error)
  
