S = '''00'''
__author__ = 'HuyNA'

import struct
import socket
import telnetlib
import hexdump
import time
import hashlib


''''

loai 0x30 (lay) 0x39 loai 0x61 (lay) 0x66 loai

(0x40 0x5b) + 0x20

0x39 < x < 0x61 =L oloai
'''


pass_size = 8
pass_buffer = ''

user_size = 8
user_buffer = ''

constant_array = ''' 70 3B 68 F3 4D DB A4 B7  46 BE 2B 38 E1 FA 6B 50
                     FC E5 F7 62 B0 77 5A 5C  D0 8C D5 1A 87 DC 12 3D
                     CD 3A 9B 7B 4A EC 4B 1E  63 1D 60 C2 78 AD F6 94
                     23 BC 97 2D 8D E3 8E 69  88 66 2C 98 9D CB 1B FB
                     20 AA 5D B1 05 61 52 F9  1F BB 04 FF 31 10 89 55
                     F1 82 7A 45 25 49 6F 64  ED 18 9E 1C D6 D3 9A F4
                     C9 C0 0F 0A E2 28 7E 33  FD 34 A0 2F 91 57 DD 03
                     27 B6 6D CE BF 01 16 43  A3 59 EF 4C DF D1 71 15
                     E0 7F 47 85 48 C4 DE 56  76 4F 53 75 5B B9 95 2A
                     09 5F 92 32 D2 6C 08 26  A5 8A 58 07 F5 51 E8 9F
                     AB D8 C3 B2 EE C7 81 44  17 80 0D D7 29 E4 A9 83
                     C1 99 E6 F0 0E 6A D4 A1  74 0B EB 3F AE 0C A6 41
                     B4 93 CA 30 35 AF 79 72  AC A8 7C BD 84 14 B5 B3
                     CC CF 9C 13 B8 C5 40 39  E7 8B 22 02 65 DA 96 F2
                     90 54 06 EA 2E 21 42 F8  C8 3E 3C %s 5E 19 D9 67
                     86 8F A2 7D 4E 6E 37 BA  73 24 E9 FE 11 A7 36 C6 ''' % S
constant_array = hexdump.restore(constant_array)


'''
       do
        {
          v23 = pass_buffer[v22];
          for ( i = 0; i < len(user_buffer); v23 = constant_array[v25] )
            v25 = (unsigned __int8)v23 ^ user_buffer[i++];
          result_array[v22++] = v23;
        }
        while ( v22 < 8 );                      //
                                                //
        v29 = 0xBAA5E82Fu;
        v30 = 0xBD0FA4A4u;
'''
