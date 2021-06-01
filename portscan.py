#!/usr/bin/env python3
#import the required modules
from socket import *
#get ip from the user
ip=input('Please Enter IP To Scan: ')
#print some verbose
print ("Scanning %s Please Wait" %ip)
#start the loop with 1000 numbers 
for port in range(1, 1000):
    #prepare the module with ipv4 tcp stream
    sock=socket(AF_INET,SOCK_STREAM)
    #make it connect to the ip and port
    ping = sock.connect_ex((ip,port))
    #verify if the connection is success or not and print the port if success.
    if(ping==0):
        print('Pord %d: OPEN' %(port))
    #close the tcp connection.
    sock.close()
