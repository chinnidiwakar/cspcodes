#!/bin/bash
figlet -ctf big  "WELCOME TO MY NETWORK SCANNER"
echo "    "
echo "(Please Wait Scanner is starting)"
echo "     "
read -p "Please Enter Your IP Range: " ip
echo "   "
figlet -ctf slant "P L E A S E  W A I T  S C A N N I N G  I S  I N  P R O G R E S S"
for i in {1..255}
do
	ping $ip$i -c 1 |grep "bytes from" | cut -d " " -f4 &
done


#/bin/bash
echo "Enter First Three Octets ex: 192.168.0. finish with a dot"
read iprange
for host in $(seq 1 254);
do arping -c 1 $iprange$host |grep "bytes from" |cut -d " " -f5;
done;

#subprocess based
#!/usr/bin/python

import subprocess
import os


netbites = raw_input("please enter the first three parts of the ip range ending with .: ")
for i in range(1, 255):
  ipaddr = netbites+str(i)
  ping = os.system("ping -c 1 %s |grep 'bytes from' > /dev/null 2>&1" %ipaddr)
  if ping == 0:
    print ipaddr
  else:
    pass


#!/bin/bash
echo "Please enter ipaddress range: "
read firstpart
for lastpart in $(seq 1 254);
do ping -c 1 $firstpart$lastpart|grep "bytes from"|cut -d " " -f4|cut -d ":" -f1;
done;

#!/bin/bash
echo  "Welcome to network scanner"
echo "  "
echo "Please enter one IP adderss from the range:"
read input
first=$(echo $input|cut -d "." -f1,2,3)
echo "  "
echo "Scanning the network please wait!!!"
echo "  "
for last in $(seq 1 254);
do
ping -c 1 $first.$last|grep "bytes from"|cut -d " " -f4;
done;


#FASTER CODE
#!/bin/bash
echo  "Welcome to network scanner"
echo "  "
echo "Please enter one IP adderss from the range:"
read input
first=$(echo $input|cut -d "." -f1,2,3)
echo "  "
echo "Scanning the network please wait!!!"
echo "  "
for last in $(seq 1 254);
do
ping -c 1 $first.$last|grep 'bytes from'|cut -d ' ' -f4 &
done;
