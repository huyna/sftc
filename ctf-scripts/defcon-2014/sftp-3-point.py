__author__ = 'HuyNA'


'''


ACCT
+Account valid, send password
USER defcon2014
-Invalid user-id, try again
PASS defcon2014
! Logged in

ACCT
  return a_write_client("+Account valid, send password");
PASS defcon2014

USER
  print(defcon valid, send account and password)

DONE
  a_write_client("+KTHXBAI!");
  exit(0);
TYPE
  a_write_client("-Not Implemented");

CDIR
  return a_write_client("-Nope");

LIST
    list file in current dir
KILL
    delete file
NAME
    rename file

STOR
  NEW
    result = a_write_client("-Filesystem does not handle generations");
  OLD
    tao file moi
      SIZE => nhap kich thuoc vao file
  APP
RETR



"/home/sftp/incoming/"



sftp

Such a simple daemon.

http://services.2014.shallweplayaga.me/sftp_bf28442aa4ab1a4089ddca16729b29ac

nc sftp_bf28442aa4ab1a4089ddca16729b29ac.2014.shallweplayaga.me 115
'''

import sys
import os
import socket
import time
import telnetlib
import struct

def recv_until(sock, delim):
    buf = ""
    while True:
        c = sock.recv(1)
        buf += c
        if delim in buf:
            break
    return buf

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
local_host="192.168.248.171"
local_port = 2323
#s.connect((local_host, local_port))

s_real = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "sftp_bf28442aa4ab1a4089ddca16729b29ac.2014.shallweplayaga.me"
port = 115
s_real.connect((host, port))

#sys.stdin.read(1)
def test_real(s):
    print recv_until(s, 'SFTP Service')
    s.send('ACCT\n')
    time.sleep(0.001)
    print recv_until(s, 'send password')
    s.send('PASS defcon2014\n')
    time.sleep(0.001)
    print recv_until(s, 'Logged in\n')

    t = telnetlib.Telnet()
    t.sock = s
    t.interact()

test_real(s_real)