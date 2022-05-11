"""#!/usr/bin/env python3
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
    print(received.psrc, received.hwsrc)"""

    
    
"""from scapy.all import *

interface = "eth0"
ip_range = "10.10.X.X/24"
broadcastMac = "ff:ff:ff:ff:ff:ff"
packet = Ether(dst=broadcastMac)/ARP(pdst = ip_range) 
ans, unans = srp(packet, timeout =2, iface=interface, inter=0.1)
for send,receive in ans:
        print (receive.sprintf(r"%Ether.src% - %ARP.psrc%"))  """



#!/usr/bin/env python3
from scapy.all import ARP, Ether, srp
nw=input("Please enter your network range: ")
arp=ARP(pdst=nw)
bdcast=Ether(dst="ff:ff:ff:ff:ff:ff")
packet=bdcast/arp
scan=srp(packet, timeout=3, verbose=0)[0]
for sent, received in scan:
    print(received.psrc, received.hwsrc)
