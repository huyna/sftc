__author__ = 'HuyNA'
import os
import socket
import time
import struct
import sys
import base64

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Exploit tasks.2014.volgactf.ru:28112
host = "tasks.2014.volgactf.ru"
local_host="192.168.248.156"
port = 28112
s.connect((host, port))
#s.connect((local_host, port))

print "press enter to continue ... "
#sys.stdin.read(1)


def recv_until(sock, delim):
    buf = ""
    while True:
        c = sock.recv(1)
        buf += c
        if delim in buf:
            break
    return buf

#print s.recv(1024)

s.send("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")

print s.recv(1024)

