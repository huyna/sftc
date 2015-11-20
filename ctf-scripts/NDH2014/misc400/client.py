#!/bin/env python

''' 
	NightlyAuth Client
'''

from __future__ import print_function
import socket

class Authentification:
    def __init__(self):
        print("Authentification started...")
        self.nonce = ""
        self.uid = 0
        self.pwd = ""

    def make_socket(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("54.217.202.218", 1337))
        return s

    def set_credentials(self,uid,pwd):
        self.uid = uid
        self.pwd = pwd

    def token_packet(self,uid,pwd):
        print("[~] Sending TOKEN Request...")
        return ("%s\x02\x01\x02\x01%s\x02\x01\x02\x01%s\x02\x01\x02\x01\x45\x4f\x53" % (1, uid, pwd))

    def auth_packet(self,uid,pwd,token):
        print("[~] Sending AUTH Request...")
        return ("%s\x02\x01\x02\x01%s\x02\x01\x02\x01%s\x02\x01\x02\x01%s\x02\x01\x02\x01\x45\x4f\x53" % (2, uid, pwd, token))

    def get_challenge(self):
        s = self.make_socket()
        s.sendall(self.token_packet(self.uid,self.pwd))
        data = s.recv(1024)
        self.nonce = data
        print("Got new challenge. Len : %s" % len(self.nonce))
        print(data)
        s.close()

    def auth(self):
        print("[~] Sending with new challenge...")
        s = self.make_socket()
        s.sendall(self.auth_packet(self.uid,self.pwd,self.nonce))
        print("Server response : %s" % s.recv(1024))
        s.close()

if __name__ == "__main__":
    print("Client started.")
    auth = Authentification()
    auth.set_credentials("","")
    auth.get_challenge()
    auth.auth()
