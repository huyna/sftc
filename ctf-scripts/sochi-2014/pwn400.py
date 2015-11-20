__author__ = 'HuyNA'
"""
Gain access to 109.233.61.11:30483. As of our previous intrusion effort, we've got a previous version of the binary.
Currently they are running a more advanced one, but hey - it's better than nothing: lhc_old.
Flag format: CTF{..32 hexes..}
"""

import sys
import os
import socket
import re
import time
import struct
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Exploit 23.23.190.205:8976 to get the flag.
host = "109.233.61.11"
local_host="192.168.248.154"
port = 30483
s.connect((host, port))
def recv_until(sock, delim):
    buf = ""
    while True:
        c = sock.recv(1)
        buf += c
        if delim in buf:
            break
    return buf
def md5_variation_collision(size, buffer):

    a = (size * 0x1337D00D) & 0xFFFFFFFF
    b = struct.pack("<I", buffer[0:4])
    temp_buffer = struct.unpack("<I", a^b) + buffer[4:]

    command = "ls \n"

    return block_1, block_2

print(s.recv(len("LHC: Ludicrous Hash Collider")+1))
print(s.recv(len("An hour of this challenge binary working costs CTF organizers $0.000001. We don't want to waste our money, so you're required to spend some cycles too.")+2))
# As the proof of work, give me 5 different blocks of length 4701 with same ZHA1 hash.
data = (recv_until(s, "\n"))
data = (recv_until(s, "\n"))
print(data)

regex = r"As the proof of work, give me 5 different blocks of length (.*) with same ZHA1 hash."
size_block = int(re.match(regex, data, re.I|re.M).group(1))
print(size_block)
command = "ls -l\n"

block_1 ="\x00"*(size_block-1)
block_2 ="b"*(size_block-1)
# Send block 0
print(s.recv(len("Send block 0")+1))
s.send(block_1+'a')
print(s.recv(len("Send block 1")+1))
s.send(block_1+'b')
print(s.recv(len("Send block 2")+1))
s.send(block_1+'c')
print(s.recv(len("Send block 3")+1))
s.send(block_1+'d')
print(s.recv(len("Send block 4")+1))
s.send(block_1+'e')

print(recv_until(s, "\n"))
print(recv_until(s, "\n"))
print(recv_until(s, "\n"))
print(recv_until(s, "\n"))
print(recv_until(s, "\n"))
print(recv_until(s, "\n"))
print(recv_until(s, "\n"))
print(recv_until(s, "\n"))
print(recv_until(s, "\n"))
print(recv_until(s, "\n"))
print(recv_until(s, "\n"))
print(recv_until(s, "\n"))
print(recv_until(s, "\n"))
print(recv_until(s, "\n"))

"""
    b *0x000000000040080E
b *0x0000000000401B7A
b *0x0000000000401B69


hash_2:     moi byte chi can giong nhau o 4 byte dau - 4 bit cuoi the nao cung dc
"""