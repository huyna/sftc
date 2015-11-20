__author__ = 'HuyNA'
import sys
import os
import socket
import time
#sys.stdin.read(1)
username = "huyna" + "\x00"*(256-len("huyna"))

case_login              = "\x01\x00\x00\x00"
case_print_all_struct   = "\x03\x00\x00\x00"
case_login = "\x01\x00\x00\x00"
case_login = "\x01\x00\x00\x00"
case_login = "\x01\x00\x00\x00"
case_login = "\x01\x00\x00\x00"

def case_1_login_init_struct(s, username):
    #result = a_read_all(userName, 0x100u);
    s.send(username)
    data = s.recv(4)
    print(data)
    if (data == 1):
        print("login: success")
    else:
        print("login error")
    return data

def case_2_delete_struct_with_index(s):
    """


    """
    index_to_delete = ""
    s.send(index_to_delete)

    result = s.recv(4)

    return result

def case_3_print_all_struct(s):

    return 1

def case_4_add_new_struct(s):
    """

    """


def case_7_write_struct_to_file(s):
    """
        + tao 1 folder moi, ten o offset +272
        + tao 1 file moi voi ten ngau nhien
        + file co cau truc
            username    | type  | size  | data
            256         | 4     | 4     | size

    """

def case_8(s):
    """
        + nhan index tu client
        + tim den struct tuong ung
        + tiep tuc nhan them 1 so nua => index trong mang data, ung voi kieu: 19 20 21
        + send data tuong ung voi tung struct len
    """
    struct_index = ""
    s.send(struct_index)
    data_index = ""
    s.send(data_index)


"""
    Moi 1 username co 1 folder tuong ung

    Trong folder do chua cac file tuong ung voi cac struct + du lieu client gui len


"""


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#184.175.99.226 9090
host = "gitsmsg.2014.ghostintheshellcode.com"
local_host="192.168.248.154"
port = 8585
s.connect((host, port))

print(s.recv(1024))
print(s.recv(1024))
print(s.recv(1024))

"""
set follow-fork-mode child
set detach-on-fork off
set
"""