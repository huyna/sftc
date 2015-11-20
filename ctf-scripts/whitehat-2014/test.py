__author__ = 'HuyNA'

import templatepwn


#s.connect(('10.0.0.1', 6007))
#s.connect(('127.0.0.1', 2307))


data_2_decode = templatepwn.read_file('D:\\obj__')
key = 'DoBGgtaiFaynDuU'

def decode(buffer_decode, key_buffer, aa):
    decode_=''
    print len(key_buffer)
    for i in xrange(len(buffer_decode)):
        c = (i + aa + len(key_buffer)) & 0xFF
        print c, ' ', hex(c)
        b = (ord(key_buffer[i % len(key_buffer)])) >> (c)
        #print hex(b)
        a = (ord(buffer_decode[i]) ^ b)
        #print chr(a)
        decode_ += chr(a)
    return decode_

def decode2(buffer_decode, key_buffer):
    decode_=''
    for i in xrange(len(buffer_decode)):
        b = (ord(key_buffer[i % len(key_buffer)])& 0xFF)
        #print hex(b)
        a = (ord(buffer_decode[i]) ^ b)
        #print chr(a)
        decode_ += chr(a)
    return decode_

#decode_buffer = decode(data_2_decode, key, 0x17)
#templatepwn.write_file('D:\\obj___', decode_buffer)


aa = 'dTqfhlu'
bb = ' cannot'

cc = decode2(aa, bb)
print cc.encode('hex')

ee = '\x6E\x22\x1D\x0A\x04\x03\x01'
ff = '\x75\x2A\x11\x0D\x04\x02\x01'
kk = '\x44\x37\x10\x08\x06\x03\x01'
gg = '\x42\x23\x19\x0E\x06\x03\x01'
pp = '\x67\x3A\x18\x0D\x04\x03\x01'
ll = '\x61\x34\x11\x0c\x07\x03\x01'
lh = '\x46\x30\x1e\x0d\x04\x03\x01'
jj = '\x79\x37\x11\x0e\x05\x02\x01'
lj = '\x44\x3a\x15\x08\x06\x02\x01'
hh = '\x55\x22\x1b\x08\x04\x03\x00'
hl = '\x55\x22\x1b\x08\x04\x03\x00'
qq = '\x47\x33\x1d\x0c\x06\x02\x00'

hh1 = '\x55\x22\x1b\x08\x04\x03\x00'
hl1 = '\x55\x22\x1b\x08\x04\x03\x00'
qq1 = '\x47\x33\x1d\x0c\x06\x02\x00'

cc = '\x00'*(32-len(ee)) + ee + '\x00'*(32-len(ff))+ff+'\x00'*(32-len(cc)) + cc



cc +=   '\x00'*(32-len(gg)) + gg + '\x00'*(32-len(pp)) + pp + \
        '\x00'*(32-len(ll)) + ll + \
        '\x00'*(32-len(lh)) + lh + \
        '\x00'*(32-len(jj)) + jj + \
        '\x00'*(32-len(lj)) + lj+\
        '\x00'*(32-len(hh)) + hh+\
        '\x00'*(32-len(hl)) + hl+\
        '\x00'*(32-len(qq)) + qq+\
        '' +\
        '\x00'*(32-len(hh1)) + hh1+\
        '\x00'*(32-len(hl1)) + hl1+\
        '\x00'*(32-len(qq1)) + qq1

print cc.encode('hex')

dd = decode2(data_2_decode[1:], cc)

templatepwn.write_file('D:\\obj_', 'M'+dd)

# 0x6e ^