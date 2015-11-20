__author__ = 'HuyNA'

""""
mll.cloudapp.net:8888 .
"""

import os
import socket
import time
import struct
import sys
import base64
def recv_until(sock, delim):
    buf = ""
    while True:
        c = sock.recv(1)
        buf += c
        if delim in buf:
            break
    return buf

host = "mll.cloudapp.net" ; port = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

data = s.recv(1024)
print data
print data.encode('hex')

data = s.recv(1024)
print data
print data.encode('hex')

data = s.recv(1024)
print data
print data.encode('hex')

# 3f061ce14ce51162d1a852d769035197172defb56118c6c5ca7c91fb30145f5a
