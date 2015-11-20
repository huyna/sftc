__author__ = 'HuyNA'

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
'''
nc wildwildweb.fluxfingers.net 1413
Note: Read the file "flag". A file that you're allowed to access is "#hello", protected with the password "passw0rd".
 socat TCP-LISTEN:1413,reuseaddr,fork EXEC:./callgate
'''
#s = socket.create_connection(('grandprix.whitehat.vn', 7007))
#s = socket.create_connection(('192.168.248.129', 1412))
s = socket.create_connection(('wildwildweb.fluxfingers.net', 1412))


buff1=''
for i in xrange(50):
    b = (0xc0+i)
    b = struct.pack('<B',b)
    c = (0x80+i)
    c = struct.pack('<B',c)
    buff1 += c+b









print ('flag{'+buff1+'}')
print 'aaaaaaaaaaaaaaaaaaaa'
aaa = 'flag{'+buff1.encode('hex')+'}'
print aaa
aa = 'flag{'+buff1+'}'
aa = aa.encode('hex')
print aa
print len(aa)
value_array = ['a','b','c','d','e','f','0','1','2','3','4','5','6','7','8','9']

buff = 'flag{'
buff = 'flag{6974736a75'
buff = 'flag{6974736a7573746c696b6'
buff = 'flag{6974736a7573746c696b65696e74686'
buff = 'flag{6974736a7573746c696b65696e7468656d6f76696'
a=(100-len(buff)-2)/2

print recv_until(s, 'guess> ')
print buff1.encode('hex')
s.send(buff1+'\n')
print recv_until(s, 'guess> ')
for j in xrange(50):
    for i in value_array:
        time.sleep(0.001)
        w = i.encode('hex')
        buff2 = buff + i
        buff2 = buff2.encode('hex')
        buff3 = buff2 + buff1[len(buff2):]
        print buff3.encode('hex')
        s.send(buff3+'\n')
        data = recv_until(s, 'guess> ')
        print data
        if "Yaaaay!" in data:
            ok = True
            break
    if ok:
        print buff3
        buff += i
        print buff
        ok = False
    else:
        print 'not . found'

# flag{6974736a7573746c696b65696e7468656d6f76696573}
'''
666c61677bbfc5bfc6bfc7bfc8bfc9bfcabfcbbfccbfcdbfcebfcfbfd0bfd1bfd2bfd3bfd4bfd5bfd6bfd7bfd8bfd9bfdabfdbbfdcbfddbfdebfdfbfe0bfe1bfe2bfe3bfe4bfe5bfe6bfe7bfe8bfe9bfeabfebbfecbfedbfeebfefbff07d
36363663363136373762bfc5bfc6bfc7bfc8bfc9bfcabfcbbfccbfcdbfcebfcfbfd0bfd1bfd2bfd3bfd4bfd5bfd6bfd7bfd8bfd9bfdabfdbbfdcbfddbfdebfdfbfe0bfe1bfe2bfe3bfe4bfe5bfe6bfe7bfe8bfe9bfeabfebbfecbfedbfeebfefbff03764
'''