__author__ = 'HuyNA'
import os
import socket
import time
import struct
import sys
import base64

def calc_hash(buffer):
    hash = ''

    for i in xrange(4):
        a = (ord(buffer[i]) ^ 0x90) & 0xFF
        hash += chr(a)

    return hash

code1 = '\xFA\xEA\xF2\xFD'  # jzbm
print calc_hash(code1)
code2 = '\xFE\xE0\xE9\xFE'  # npyn
print calc_hash(code2)

p1 = 'jzbm'
p2 = 'npyn'

const_string = '0123456789abcdefghijklmnopqrstuvwxyz'
size_const_string = len(const_string)

final=''

for i in p1:
    a = const_string.index(i)
    t = size_const_string - 1 - a
    print t,'\t',

    a = const_string[t]
    print a,'\t',
    a = a.encode('hex')
    final += a
    print a


for i in p2:
    a = const_string.index(i)
    t = size_const_string - 1 - a
    print t,'\t',

    a = const_string[t]
    print a,'\t',
    a = a.encode('hex')
    final += a
    print a

print final

#67306F6463613163
#67306f6463613163