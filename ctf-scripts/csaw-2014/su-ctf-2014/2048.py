__author__ = 'HuyNA'


'''

'''
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

data = pi(2014)
data += pi(1)
data += pi(0)
print data
print data.encode('hex')
md5_ = hashlib.md5(data).hexdigest()

print 'ctf.sharif.edu:2048/'+md5_+'/target.txt'

# current 1411781128
# need76

'''
Terminate Me
reverse  forensics

Terminate me and unload the driver to get the flag!
Flag : md5 [string in theFlag.txt file!]
Notes:
1- use windows 7/8 64 bit
2- turn off your antivirus

Download
.text:0000000140001430 168 mov     dword ptr [rbp-30h], 92959991h
.text:0000000140001437 168 mov     [rbp+60h+var_8C], 92969793h
.text:000000014000143E 168 mov     [rbp+60h+var_88], 92919794h
.text:0000000140001445 168 mov     [rbp+60h+var_84], 93919192h
.text:000000014000144C 168 mov     [rbp+60h+var_80], 99949897h
.text:0000000140001453 168 mov     [rbp+60h+var_7C], 92929198h
.text:000000014000145A 168 mov     [rbp+60h+var_78], 92919698h
.text:0000000140001461 168 mov     [rbp+60h+var_74], 91969698h
.text:0000000140001468 168 mov     [rbp+60h+var_70], 60h
'''

data = pi(0x92959991-0x60606060)
data += pi(0x92969793-0x60606060)
data += pi(0x92919794-0x60606060)
data += pi(0x93919192-0x60606060)
data += pi(0x99949897-0x60606060)
data += pi(0x92929198-0x60606060)
data += pi(0x92919698-0x60606060)
data += pi(0x91969698-0x60606060)

print data



'''
Hooked API
forensics

Load me and Analyze the memory changes!
flag: MD5[LowerCase[Hooked API's Name]]
Req : Windows 7/8 32 bit
username: phd.team-1 password: hTt707eTIo
[2:54:16 PM] *** username: phd.team-1 password: hTt707eTIo ||
http://ctf.sharif.edu/2014/quals/su-ctf/panel/
username: phd.team-2 password: 4MZCJ4pMws ||
username: phd.team-3 password: nu7oMXs6q9" ***
'''

print hashlib.md('ntunloaddriver').hexdigest()