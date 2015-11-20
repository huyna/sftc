__author__ = 'HuyNA'


"""
nc 210.71.253.109 9123
"""
import sys
import os
import socket
import time
import telnetlib
import struct

def recv_until(sock, delim):
    buf = ""
    while True:
        c = sock.recv(1)
        buf += c
        if delim in buf:
            break
    return buf
# nc 210.61.8.96 51342
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
local_host="210.71.253.109"
#local_host='192.168.248.176'
local_port = 9123


