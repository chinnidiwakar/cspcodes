#!/bin/bash
echo  "Welcome to port scanner\n"
read -p "Please enter IP adderss" input
echo "\nScanning the ports Please wait!!!!!"
nc -nvz $input 1-65534 > /tmp/file.txt 2>&1
cat /tmp/file.txt |grep "UNKNOWN"|cut -d " " -f3,5|tac
