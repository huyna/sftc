__author__ = 'HuyNA'
"""
sass
Pwnables (200 pts)
Not all of The Plagues services seem secure. Getting into this one, might give us some clues as to when he is planning to time jump to next.
The service is at 54.198.50.139:5455;
you may also want to ssh to ctf@54.198.50.139 (password: ctf) to debug your exploits in the local environment. Read the README_SASS there!
"""

import os
import socket
import time
import struct
import sys
import base64

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "54.198.50.139"
local_host="192.168.248.172"
port = 5455
s.connect((host, port))

def recv_until(sock, delim):
    buf = ""
    while True:
        c = sock.recv(1)
        buf += c
        if delim in buf:
            break
    return buf

s.send("12345\n")
s.send("\n")

print recv_until(s, "\n")
