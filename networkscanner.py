#!/usr/bin/env python
#import necessary functions from scapy
from scapy.all import ARP, Ether, srp
#take input from user
nw=input("Please Enter Network Range: ")
#make a arp packet with ARP function and user data
arp=ARP(pdst=nw)
#define a broadcast ip
brdcst= Ether(dst="ff:ff:ff:ff:ff:ff")
#build the packet
packet= brdcst/arp
#make a blank dictionary to save the output
clients = []
#prepare the packet with all the necessary info using srp
result = srp(packet, timeout=3, verbose=0)[0]

#loop and send packets and get data and add that to your dictionary
for sent, received in result:
    clients.append({'ip': received.psrc, 'mac': received.hwsrc})

#print the info fromt he dictionary
print ("Printing Available Devices In the Target Network: ")
for device in clients:
    print(device['ip'],device['mac'])
