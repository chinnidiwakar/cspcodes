#!/usr/bin/python3
import requests 
import sys 

global host, wordlist

try:
    host=input("\nPlease Enter The Server Domain/IP: ")
    wordlist=input("\nPlease Enter Password Dictionary With Full Path: ")
    if os.path.exists(wordlist) == False:
        print("\nFile Doesnt Exists :(")
        sys.exit()
    else:
        print("\nLoading The Password File :)")
except KeyboardInterrupt:
   print("\nUser Stopped The Script :(")
   sys.exit()

sub_list = open(wordlist).read() 
directories = sub_list.splitlines()

for dir in directories:
    dir_enum = f"http://{sys.argv[1]}/{dir}.html" 
    r = requests.get(dir_enum)
    if r.status_code==404: 
        pass
    else:
        print("Valid directory:" ,dir_enum)
