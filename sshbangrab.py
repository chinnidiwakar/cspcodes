#!/usr/bin/python3
import socket
bangrab = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
bangrab.connect(("IP",22))
bangrab.recv(4096)
exit()
