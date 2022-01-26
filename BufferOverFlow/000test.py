#!/usr/bin/env python2
import socket
#setup the ip and port we are connecting to
RHOST = "192.168.0.120"
RPORT = 31337
#create a tcp connection(socket)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((RHOST,RPORT))
#build a happy little message followed by a newline
buf = ""
buf += "Python Script"
buf += "\n"
#send the happy little message down the socket
s.send(buf)
#print out what we sent
print "Sent: {0}".format(buf)
#receive some data from the socket
data = s.recv(1024)
#print out what we received
print "Received: {0}".format(data)
