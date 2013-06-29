#!/usr/bin/python
__author__ = 'Mitchell'
import socket
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    sock.connect(('google.com', 80))
except:
    print("FAIL")
