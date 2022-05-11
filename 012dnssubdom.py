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
subdoms = sub_list.splitlines()

for sub in subdoms:
    sub_domains = f"http://{sub}.{sys.argv[1]}" 

    try:
        requests.get(sub_domains)
    
    except requests.ConnectionError: 
        pass
    
    else:
        print("Valid domain: ",sub_domains)

        
        
        
"""#!/usr/bin/env python3
import requests
host=input("\nPlease enter your target Domain name: ")
subs=open("/root/PycharmProjects/pythonProject/dictionary.txt", "r").read()
doms=subs.splitlines()
for xyz in doms:
    try:
        requests.get("http://"+xyz+"."+host)
        print("http://"+xyz+"."+host)
    except requests.ConnectionError:
        pass
