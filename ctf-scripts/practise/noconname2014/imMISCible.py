__author__ = 'HuyNA'

import os
import marshal
import new
import hashlib
import base64
import hexdump
import socket
import telnetlib

# 88.87.208.163:6969
# 11111111111111111
def xor_encrypt(data, key):
    decode_string = ''
    for i in range(len(data)):
        decode_string += chr((ord(data[i])^ord(key[len(key)-i%len(key)-1]))&0xFF)
    return decode_string

data='55 75 44 B6 0B 33 06 03 E9 02 60 71 47 B2 44 33'
data1=hexdump.dehex(data)
print data.encode('hex')
key='65 87 33 45 12'
key1=hexdump.dehex(key)



flag=xor_encrypt(data1,key1)
print flag.encode('hex')
print flag
print hashlib.sha1(flag).hexdigest()
a='01101111080101100801101010110101'.decode('hex')
print hashlib.sha1(a).hexdigest()
s = socket.create_connection(('88.87.208.163', 6969))
t = telnetlib.Telnet()
t.sock = s
t.interact()

