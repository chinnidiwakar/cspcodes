#!/usr/bin/env python3
from socket import *
ip=input('Please Enter IP To Scan: ')
print ("Scanning %s Please Wait" %ip)
for port in range(1, 1000):
    sock=socket(AF_INET,SOCK_STREAM)
    ping = sock.connect_ex((ip,port))
    if(ping==0):
        print('Pord %d: OPEN' %(port,))
    sock.close()
