__author__ = 'HuyNA'
"""
    ← Quest server
        telnet://vuln1.quals.ructf.org:16710 binary
        Flag format is "RUCTF_.*".
"""
import os
import socket
import time
import struct
import sys
import base64
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Exploit 23.23.190.205:8888 and read flag.txt
host = "vuln1.quals.ructf.org"
local_host="192.168.248.157"
port = 16711
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


recv_until(s, "> ")

"""
    banner.txt
        Touhou Level Pack Demo

This level pack is in beta-test stage.
Please purchase the 'Early bird package' to unlock the locked levels and gain access to the new level releases.

Select level:

(1) Intro
(2) The Hakurei Shrine (Locked!)
(-1) Quit
"""

