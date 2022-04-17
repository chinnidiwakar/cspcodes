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
