#!/bin/bash
#Take Input
#printf "Please Enter Domain Name: "
#read domain
#DNS Resolve
#printf "Host Name Is : \n"
#host -t a $domain|grep "has address"|cut -d " " -f 4
#NS Extraction
#printf "Nameservers Are : \n"
#host -t ns $domain|grep "name server"|cut -d " " -f 4 > /tmp/ns.txt
#cat /tmp/ns.txt | while read line; do host -t a $line; done|grep "has address"|cut -d " " -f 4
#MS Extraction
#printf "Mail Exchange Servers Are : \n"
#host -t mx hackerschool.in|grep "is handled"|cut -d " " -f 7 > /tmp/mx.txt
#cat /tmp/mx.txt | while read line; do host -t a $line; done|grep "has address"|cut -d " " -f 4



#!/bin/bash
#read -p "Please Enter Your Target Domain Name: " dom
#echo "                          "
#echo "Printing Domain and its IP"
#echo "=========================="
#host -t A $dom|grep "has address"|cut -d" " -f1,4
#echo "                          "
#echo "                          "
#echo "Printing Name Servers and Their IPs"
#echo "=========================="
#host -t NS $dom|grep "name server"|cut -d " " -f4 | while read nameserver; do host -t A $nameserver|grep "has address"|cut -d " " -f1,4;done
#echo "                          "
#echo "                          "
#echo "Printing Mail Exchange Servers and Their IPs"
#echo "=========================="
#host -t MX $dom|grep "handled by"|cut -d " " -f7 |while read mailex;do host -t A $mailex|grep "has address"|cut -d " " -f1,4;done



#Take Input
printf "Please Enter Domain Name: "
read domain
space='\t'

#DNS Resolve
printf "\nHost Name Is : \n\n"
hostname=$(host -t a $domain|grep "has address"|cut -d " " -f 4)
printf $domain'%-10s%-4s'$hostname'\n\n' 


#NS Extraction
printf "\nNameservers Are : \n\n"
host -t ns $domain|grep "name server"|cut -d " " -f 4| while read line; do printf $line'%-10s%-4s';host -t a $line|grep "has address"|cut -d " " -f4; done
printf "\n"


#MS Extraction
printf '\n'
printf "Mail Exchange Servers Are : \n\n"
host -t mx $domain|grep "is handled"|cut -d " " -f 7| while read line; do printf $line'%-10s%-14s';host -t a $line|grep "has address"|cut -d " " -f4; done





#!/bin/bash
echo "Welcome to dnsenumerator"
echo "  "
echo "please enter a domain name: "
read domain
echo "  "
echo "enumerating domains info please wait !!!"
echo "  "
echo "Printing IPs of the "$domain
host -t A $domain|grep "has address"|cut -d " " -f4
echo "  "
echo "Printing NS Info of the "$domain
host -t NS $domain|grep "name server"|cut -d " " -f4|while read naresh;do echo $naresh;host -t A $naresh|grep "has address"|cut -d " " -f4;done
echo "  "
echo "Printing MX Info of the "$domain
host -t MX $domain|grep "handled by"|cut -d " " -f7|while read mahesh;do echo $mahesh;host -t A $mahesh|grep "has address"|cut -d " " -f4;done


#CHINNI
