#!/usr/bin/env python

from scapy.all import ARP, Ether, srp

nw=input("Please Enter Network Range: ")

arp=ARP(pdst=nw)

brdcst= Ether(dst="ff:ff:ff:ff:ff:ff")

packet= brdcst/arp

clients = []

result = srp(packet, timeout=3, verbose=0)[0]

for sent, received in result:
    clients.append({'ip': received.psrc, 'mac': received.hwsrc})


print ("Printing Available Devices In the Target Network: ")
for device in clients:
    print(device['ip'],device['mac'])
