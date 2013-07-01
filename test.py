#!/usr/bin/python
__author__ = 'Mitchell'
import socket
from threading import Thread
IPs = '192.168.112.'





for ip in range (60,86):
    try:
        sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        sock.setblocking(0)
        test = IPs + str(ip)

        sock.connect((test, 3389))
        print(IPs + str(ip) + ' NCJBOD' + str(ip-50))
        sock.close()
    except socket.error as msg:
        print(IPs + str(ip), msg)
        sock.close()

