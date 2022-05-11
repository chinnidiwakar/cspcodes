"""

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

    
    
import sys
import socket
import pyfiglet


ascii_banner = pyfiglet.figlet_format("TryHackMe \n Python 4 Pentesters \nPort Scanner")
print(ascii_banner)


ip = '192.168.1.6' 
open_ports =[] 

ports = range(1, 65535)


def probe_port(ip, port, result = 1): 
  try: 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    sock.settimeout(0.5) 
    r = sock.connect_ex((ip, port))   
    if r == 0: 
      result = r 
    sock.close() 
  except Exception as e: 
    pass 
  return result


for port in ports: 
    sys.stdout.flush() 
    response = probe_port(ip, port) 
    if response == 0: 
        open_ports.append(port) 
    

if open_ports: 
  print ("Open Ports are: ") 
  print (sorted(open_ports)) 
else: 
  print ("Looks like no ports are open :(") """

    
    
#!/usr/bin/env python3

#install the below components
#sudo apt-get install python3-pip
#python3 -m pip install --upgrade pip
#python3 -m pip install validators
#pip3 install validators

#import necessary modules
import ipaddress
import validators
from socket import *

#take input
ipdom=input("Please Enter Your Target IP: ")

try:
    #validate the ip
    ip=ipaddress.ip_address(ipdom)
    print ("\nPlease wait while ports are being scanned\n")
    #Scan for ports in loop
    for port in range(1,65535):
        s=socket(AF_INET,SOCK_STREAM)
        conn=s.connect_ex((str(ip),port))
        if(conn==0):
            print('Port %d: OPEN'%(port))
        s.close()
except ValueError:
    #validate the domain
    if(validators.domain(ipdom)==True):
        print ("\nPlease wait while ports are being scanned\n")
        #Extract IP of the domain
        ip=gethostbyname(ipdom)
        #Scan for ports in loop
        for port in range(1,65535):
            s=socket(AF_INET,SOCK_STREAM)
            conn=s.connect_ex((str(ip),port))
            if(conn==0):
                print('Port %d: OPEN'%(port))
            s.close() 
    else:
        #Print Error.
        print ("Please enter a valid IP/Domain")
