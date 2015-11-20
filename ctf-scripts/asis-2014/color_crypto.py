#!/usr/bin/env python

import Image
import random


def get_color(x, y, r):
    n = (pow(x, 3) + pow(y, 3)) ^ r
    return (n ^ ((n >> 8) << 8 ))


flag_img = Image.open("flag.png")
im = flag_img.load()
r = random.randint(1, pow(2, 256))
print flag_img.size
print r
enc_img = Image.new(flag_img.mode, flag_img.size)
enpix = enc_img.load()
for x in range(flag_img.size[0]):
        for y in range(flag_img.size[1]):
            enpix[x, y] = 0
enc_img.save('test'+'.png')

def brute(r):
    flag_img1 = Image.open("test.png")
    enpix1 = flag_img1.load()
    for x in range(flag_img.size[0]):
        for y in range(flag_img.size[1]):
            if im[x, y] >= 250:
                s = get_color(x, y, r)
                #if s>0: s=255
                enpix1[x, y] = s
                if enpix[x,y] == 0: enpix[x,y] = 255

            #print s

    flag_img1.save('enc'+str(r)+'.png')

for i in xrange(256):
    brute(i)
    print i

enc_img.save('last'+'.png')
## ASIS_af4e8acbbcacef44fd3ecdbc6e9696de
## ASIS_af4e8acbbeacef44fd3ecdbe6e9696de
## ASIS_af4e8acbbcacef44fd3ecdbc6e9696d4
## ASIS_af4e8acbbcacef44fd3ecdbc6e9695de