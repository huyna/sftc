__author__ = 'HuyNA'

import itertools
import hexdump

def xor_encrypt(data, key):
    decode_string = ''
    for i in range(len(data)):
        decode_string += chr((ord(data[i])^ord(key[i%len(key)]))&0xFF)
    return decode_string
def beauty_print(data):
    hexdump.hexdump(data)

def re3():
    xor1 = '\x2c\x09\x3d\x04\x47\x66\x0c\x10'
    xor2 = '\x6f\x59\x0a\x64\x09\x52\x02\x5c'
    xor3 = '\x6f\x4e\x00\x56\x66\x56\x02\x14'
    ma = 'sxbzuiS{ylfa490'
    s1 = 'sbS409aiflxuzy'
    in_order = '049Sabfilsuxyz{'
    pre_order = 'sbS409aiflxuzy{'
    post_order = '094aSflibuy{zxs'

    print xor_encrypt(xor1,pre_order)
    print xor_encrypt(pre_order,xor1)
    print xor_encrypt(xor2,in_order)

    print xor_encrypt(xor3,post_order)
    data= xor_encrypt(post_order,xor3)
    print data
    beauty_print(data)
    print len(data)


re3()
#'0\x08\x05abcdefgh ijklmno  pqrstuvw xyzABCD  EFGHIJKL MNOPQRS'
#'                        pqrstuvwxyzABCD EFGHIJKLMNOPQRS'
#main tree
'sxbzuiS{ylfa490'

'''
'fla9{y0u_kn0w_my_m37h0d5_w4750n}'

'0'
'\x08'
'\x05'
'd'*8
'b'*8
'c'*8



xor string1 3
                                           DCB 0x2C ; ,            ; DATA XREF: BST::stage4_check(char
.data:0000000000496541                     DCB    9
.data:0000000000496542                     DCB 0x3D ; =
.data:0000000000496543                     DCB    4
.data:0000000000496544                     DCB 0x47 ; G
.data:0000000000496545                     DCB 0x66 ; f
.data:0000000000496546                     DCB  0xC
.data:0000000000496547                     DCB 0x10


xor string 2 18
.data:0000000000496550     fifth_str       DCB 0x6F ; o            ; DATA XREF: BST::stage5_check(char
.data:0000000000496550                                             ; BST::stage5_check(char *)+64o
.data:0000000000496551                     DCB 0x59 ; Y
.data:0000000000496552                     DCB  0xA
.data:0000000000496553                     DCB 0x64 ; d
.data:0000000000496554                     DCB    9
.data:0000000000496555                     DCB 0x52 ; R
.data:0000000000496556                     DCB    2
.data:0000000000496557                     DCB 0x5C ; \

xor string 3 33
.data:0000000000496560     sixth_str       DCB 0x6F ; o            ; DATA XREF: BST::stage6_check(char
.data:0000000000496560                                             ; BST::stage6_check(char *)+68o
.data:0000000000496561                     DCB 0x4E ; N
.data:0000000000496562                     DCB    0
.data:0000000000496563                     DCB 0x56 ; V
.data:0000000000496564                     DCB 0x66 ; f
.data:0000000000496565                     DCB 0x56 ; V
.data:0000000000496566                     DCB    2
.data:0000000000496567                     DCB 0x14


6th     => [0-9a-f]
17th    => string.punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

18th    => xdigit
32th    => punctuation

9th    => xdigit
44th    => punctuation

22th    => xdigit
31th    => lower

47th    => lower
34th    => upper
'''