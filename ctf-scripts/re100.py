__author__ = 'HuyNA'

# Embedded file name: RE100.py
import string
import sys, base64
import socket
import time
def main():
    zData = '4ba1aea4b05baabfb6ac4aaeb8b6ac5db6b9a5bca3ac48a5aea1a1aaa3a4aab2'.decode('hex')
    print 'Enter your Secret number: '
    sNum = int(raw_input())
    t1 = sNum / 100
    t2 = sNum % 100
    zRe = ''
    for i in zData:
        zRe += chr(((ord(i) ^ t2) + t1) % 256)

    print 'Here your flag: ', zRe

def decrypt():
    zData = '4ba1aea4b05baabfb6ac4aaeb8b6ac5db6b9a5bca3ac48a5aea1a1aaa3a4aab2'.decode('hex')

    for j in xrange(255):
        for i in xrange(99):
            zRe = ''
            for x in zData:
                zRe += chr(((ord(x) ^ i) + j) % 256)
            print zRe

def re200():
    data = "FbaMiWfbuycfuQqKnGQlgZrhmzXhmUdxFeMiXfNuUGWaLMPXJcYpRKmRODtLqUUoeBuAuexTgnQcZSqrVzwurIzigdOAjiQaVCGiaiTKnIsegMfoblTNqD_NZqYZatZYNKBgQHUhacXgOMQaQeTGLkXEepxsUrEDhrjBYKSXWSBcImqYsEWevgUPfRvtEVdVhnQEdfmEEGmSCbxjZTUmiwZdMtVMYploEeteMuIAVhELPToYKdalIiEMCCFQiMtqHIYZKClvcDWuMBizAmDiXahtTcYVjkxretIOjBaocIknMiWecowZyMqfQgtHtcoobupVeGlXmUQOVAAIalNMecWCdJLi_PhzLTocjjkSFAPLGrnosKIZTKwLuotErtWwLFEjfBQWaQdsDdeNvChmgDeDXbhBiDTYJMJFbQwTZOTFBWObYfcMREAirAPEJsxlUGJijDIMoMxhxmjdZrYyoLiisFxcNsqoitvWSPVkFgumQfKYsNJbjHTonceVCZjLHxVppBWLvmshSrFiBAeqUGfPhrDupGCDWAFCBYvCBnyPfLsUWOWZtTWLBPogtmetsdWVylmAfVEzSAUhcHZEkEwfmxTzlrzcBjRMVFhtIDcyWlpartBuMJIvHIEZxbfbddTUleQPikvQWTSzaIofpEI_xclNKmLhnYejHUeqoIHMpmYFynubeGwvflwwYrNTFdJMxcescaSiYINxdirgxKSUlwEmobLEiNBZFCMgEbMgnQxLLoviEqVuxtWGmJBIHvuotUbhHynCiaSWhveAGBMOlKMspWqHCngWrw{aKUoTUeocPtPsbWdTWpSwCGspEKcEIjuVdOCGXXlPxJsqsjBAOBTfMklrrBmjSLQrzfBcWvgJQopbwuGAhZhjtaWLCqtXetEVQFTHySwFugbhHWBoDkdiXJKyucIj}kofGuJpfEjDwkbMcSPqGpNJoHQICIDwdCc_DeTiNHfeRkdwRrjVScxaPC_QCSqfzLeM"
    prime = [2,3,5,7,11,13]
    for i in range(1000, 2000):
        flag=''
        for j in range(0,6):
            t = i / prime[j]
            d = i % prime[j]
            while d < 1000:
                flag += data[d]
                d += t
        print str(i) + ": " + flag

def oOOo(key, clear):
    O0 = []
    for o0O in range(len(clear)):
        iI11I1II1I1I = key[o0O % len(key)]
        oooo = chr((ord(clear[o0O]) + ord(iI11I1II1I1I)) % 256)
        O0.append(oooo)

    return base64.urlsafe_b64encode(''.join(O0))

def connect_server(key, ss):
    host = 'ctf.whitehat.vn'
    port = 1365
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect((host, port))
    send_data = oOOo(key,ss)
    #print ss
    #print send_data
    s.sendall(send_data)

    begin = time.time()
    OoOoOO00 = s.recv(1024)
    end = time.time()

    #print end-begin

    print OoOoOO00
    s.close()

if __name__ == '__main__':
    #re200()
    #main()
    key = 'whitehatcontest'
    b1 = "Flag{aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa}FbbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaFbbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaFbbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    b2 = "Flagaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    b3 = "FbbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaFbbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaFbbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaFbbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    b4="Flag"
    b5="Fl"
    for i in string.printable:
        connect_server(key, i)

"""
    Flag{aaaaaaaaaaaaaaaaaa}    RmxhZ3thYWFhYWFhYWFhYWFhYWFhYWF9    0279998779297
    Faaaaaaaaaaaaaaaaaaaaaaa    RmFhYWFhYWFhYWFhYWFhYWFhYWFhYWFh
    Flbbbbbbbbbbbbbbbbbbbbbb    RmxiYmJiYmJiYmJiYmJiYmJiYmJiYmJi
    Flaaaaaaaaaaaaaaaaaaaaaa    RmxhYWFhYWFhYWFhYWFhYWFhYWFhYWFh
    Flagaaaaaaaaaaaaaaaaaaaa    RmxhZ2FhYWFhYWFhYWFhYWFhYWFhYWFh    0269999504089


    Flag{aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa}
    Flagaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    Faaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
"""
# Flag{Very_Easy_Python_Challenge}
# Flag{MIPS_is_very_easy_to_understand}

# FvasLFYrpQbEHsJeDFaEMvjmYCeujsKdBHkomx}
# FvasLFYrpQbEHsJeDFaEMvjmYCeujsKdBHkomx}