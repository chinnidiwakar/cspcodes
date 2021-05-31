#!/usr/bin/env python3
a=int(input("How many times you want to print: "))
for x in range(0, a):
    print("We're on time %d" % (x))
for x in range(0,a):
    print("192.168.0.%d"%(x))
for ip in range(0, 255):
    print("192.168.0."+str(ip))
