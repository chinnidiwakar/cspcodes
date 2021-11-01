#!/usr/bin/env python3
#take input from user
range=input("Please Enter Network Range: ")
#print the info fromt he dictionary
print ("Printing Available Devices In the Target Network: \n")
#import necessary functions from scapy
from scapy.all import ARP, Ether, srp
#make a arp packet with ARP function and user data
arp=ARP(pdst=range)
#define a broadcast ip
bdcast=Ether(dst="ff:ff:ff:ff:ff:ff")
#build the packet
packet= bdcast/arp
#make a blank dictionary to save the output
targets= []
#prepare the packet with all the necessary info using srp
gotip=srp(packet, timeout=3, verbose=0)[0]
#loop and send packets and get data and add that to your dictionary
for sent, received in gotip:
    print(received.psrc, received.hwsrc)
