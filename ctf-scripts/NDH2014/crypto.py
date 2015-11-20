__author__ = 'HuyNA'
import os
import socket
import time
import struct
import sys
import base64
import re
# crypt 50 1
binary_string = '00010111000001110001010001100011 00001001000111010000001000001000 01110001000001010000000000000011 01100011000110110001100100001010 00011100011100010000000000000111 00010000000011110110111100011000 00010000011011110001011100001111 00000000000100100000000000000110 00011111000000100001101000010010 00001010000000010001100000001011 00000110000111010000101000011111 00011000000011110000011000010111 00001010000011000001000000010111 00000110000111100000110101100001'

# crypto250
"""
PsCrypto
Here is a new cloud service named "PsCrypto™ ", it is used by many influental people. You can access your data with the login :"ulysse" and the password "penelope". The server adress is 54.217.202.218 and the port is 2609.

A friend just gave you a file named "dumpusersps.txt", in this file you have a small list of PsCrypto™ users.

Your mission is to find the flag stored in a file of a specific user.

chay python client.py 54.217.202.218 2609 ulysse penelope get dump_users_ps.txt
lay dc:
kim_jong-un
michael-rogers
ulysse
vladimir-poutine

python client.py 54.217.202.218 2609 kim_jong-un penelope ls
password
about.txt
terrorists_keywords.txt
ufo_case.txt
Mail-1.txt

python client.py 54.217.202.218 2609 kim_jong-un penelope ls
password
propaganda.txt
nuclear_targets.txt
un_decision_answer.png
nuclear_launcher_production_project.jpg

python client.py 54.217.202.218 2609 vladimir-poutine asasasasa ls
password
mail-1.txt
crimea_invasion.txt
meonabear.jpeg
invasion_plan.jpg
nuclear_code.txt
poutine.jpg

   16
(0, 0, 65, 0, 0, 0, 19, 0, 87, 1)
[41, 65, 110, 174, 38, 14, 60, 17]
[73, 32, 108, 111, 118, 101, 32, 80, 111, 110, 105, 101, 115, 32, 97, 110, 100, 32, 85, 110, 105, 99, 111, 114, 110, 115]

"""


# crypto 300
"""
    This is a crypted image, you must extract the data.

Score
300
Link
http://static.nuitduhack.com/crypted.bmp

"""
cipher = '\xFB\x5E\xA1\xB7\x89\x5C\x5E\x8D\xA7\x5A\x0D\xDF\x03\x00\xFE\x3B'
plain = '\xFF'*16
plain1 = "BM"+struct.pack("<I",0x0041EB40)+"\x00"*4+struct.pack("<I",0x00000036)+"\x28\x00\x00\x00"
key = ''

def decrypt(data, key):
    size = len(data)
    key_size = len(key)
    return_data = ""
    for i in xrange(size):
        a = data[i]
        b = key[i % key_size]
        c = ord(a) ^ ord(b)
        return_data += chr(c)
    return return_data

# open file
path_file = "D:\\ViecTrenTT\\skydrive\\ARM_Assembly\\Tools\\crypto300\\imagedata.bmp"
plain_file = "D:\\ViecTrenTT\\skydrive\\ARM_Assembly\\Tools\\crypto300\\plain.bmp"
folder = "D:\\ViecTrenTT\\skydrive\\ARM_Assembly\\Tools\\crypto300\\a\\"
f = open(path_file, 'rb')
filename = "aaa"
header = '\x42\x4D\x40\xEB\x41\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\xB0\x04\x00\x00\xAF\x04\x00\x00\x10\x00\x18\x00\x00\x00\x00\x00\x0A\xEB\x41\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
data = f.read()
#print data.encode("hex")
# find key


for i in range(0, 100):
    plain = chr(i)*16
    key = decrypt(cipher, plain)
    print key.encode("hex")
    temp = folder+filename+str(i) + ".bmp"
    plain = decrypt(data, key)
    plain = header + plain
    fou = open(temp, 'wb')
    fou.write(plain)
    fou.close()
    print temp
f.close()