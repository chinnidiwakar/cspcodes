#!/usr/bin/env python3
data=input("Please Enter a letter: ")
if type(data) == True :
    print ("it is a text value")
else:
    print ("It is not a text value")
try:
    data2=int(input("Please enter port: "))
except ValueError:
    print ("not a number")
    exit()
if data2 < 65535 and data2 > 0:
    print ("it is a valid port")
else:
    print ("it is invalid port")
