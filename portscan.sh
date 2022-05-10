#!/bin/bash
echo  "Welcome to port scanner\n"
read -p "Please enter IP adderss" input
#in ZSH read "?prompt: " input
echo "\nScanning the ports Please wait!!!!!"
while :;do for s in / - \\ \|; do printf "\r$s";sleep .1;done;done
nc -nvz $input 1-65534 > /tmp/file.txt 2>&1
cat /tmp/file.txt |grep "UNKNOWN"|cut -d " " -f3,5|tac
