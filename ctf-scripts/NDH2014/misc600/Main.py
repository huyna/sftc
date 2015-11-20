#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import curses
import socket
import chat_protocol_pb2
from curses.textpad import rectangle
from struct import pack
import threading

class NetWrapper:
    def __init__(self):
        pass

    def connect(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(("46.231.151.147", 4567))
            self.socket = s
            return True
        except:
            return False

    def auth(self,username):
        authpacket = chat_protocol_pb2.AuthPacket()
        authpacket.username = username
        self.username = username
        data = "1" + authpacket.SerializeToString()
        self.socket.send(pack('<I', len(data)) + data)

    def wait_authresponse(self):
        authresponse = chat_protocol_pb2.TokenResponse()
        authresponse.ParseFromString(self.socket.recv(1024))
        if authresponse.authstatus == 1:
            self.token = authresponse.token
            return True
        else:
            return False

    def sendmessage(self,msg):
        if len(msg) < 2:
            return
        usermessage = chat_protocol_pb2.ChatMessage()
        usermessage.cookie = self.token
        usermessage.nickname = self.username
        usermessage.textmessage = msg
        data = "2" + usermessage.SerializeToString()
        self.socket.send(pack('<I', len(data)) + data)

class ThreadRecv(threading.Thread):
    def __init__(self,sock,curses):
        threading.Thread.__init__(self)
        self.sock = sock
        self.curses = curses

    def run(self):
        while True:
            data = self.MSGDecoder((self.sock.recv(1024)))
            try:
                self.curses.addmessage((data[0] + " : " + data[1]).encode(encoding='UTF-8',errors='replace'))
            except:
                pass

    def MSGDecoder(self,data):
        msg = chat_protocol_pb2.ChatMessage()
        msg.ParseFromString(data)
        return (msg.nickname, msg.textmessage)

class CurseUI:
    def __init__(self):
        self.screen = curses.initscr()
        self.screen.clear()
        self.screen.border(0)
        curses.start_color()
        self.error = 1
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
        self.success = 2
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
        self.usertext = 3
        curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK)
        self.connecting = 4
        curses.init_pair(4, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
        self.NetWrap = NetWrapper() #Classeption
        self.msgoffset_x = 4
        self.msgoffset_y = 3
        self.msgcount = 0
        self.size = self.screen.getmaxyx()

    def addtext(self,text,offset_x=2,offset_y=False, color=0):
        self.screen.addstr(offset_x, offset_y, text, curses.color_pair(color))
        self.screen.refresh()

    def addmessage(self,text):
        maxsize = self.screen.getmaxyx()[0] - 5
        if (self.msgoffset_x > maxsize):
            self.screen.clear()
            self.drawchat()
            self.msgoffset_x = 4
        self.screen.addstr(self.msgoffset_x, self.msgoffset_y, text)
        self.msgoffset_x += 1
        self.screen.refresh()
        self.drawchat()

    def get_param(self,prompt_string):
        #self.screen.clear()
        self.addtext(prompt_string, 2, 2)
        self.screen.refresh()
        return self.get_input()

    def get_input(self,offset_x=10,offset_y=10,maxsize=60):
        return self.screen.getstr(offset_x,offset_y,maxsize)

    def get_username(self):
        self.addtext("Please, enter a nickname : ",4,4)
        self.username = self.get_input(offset_x=4,offset_y=31)
        return self.username

    def connect(self):
        self.addtext("Ok " + self.username + " ! Connecting to Nibble's Server...",7,2)
        if not self.NetWrap.connect():
            self.addtext("Can't connect to Nibble's Server...",8,4)
            time.sleep(2)
            return

        self.addtext("Sending Auth Packet...",10,4)
        self.NetWrap.auth(self.username)
        self.addtext("Awaiting Auth Response...",12,4)
        response = self.NetWrap.wait_authresponse()
        if response:
            self.addtext("OK ! You are online !",14,4,self.success)
        else:
            self.addtext("Authentification failed...",14,4,self.error)
        time.sleep(2)
        recvthread = ThreadRecv(self.NetWrap.socket,self)
        recvthread.start()
        return True

    def drawchat(self):
        #self.screen.clear()
        self.screen.border(0)
        self.addtext("Nibble's Chat Client - Connected", 1, 2, 2)
        self.size = self.screen.getmaxyx()
        rectangle(self.screen, 2,1, self.size[0] - 3,self.size[1]-2)
        self.addtext(" "*(self.size[1]-3),    self.size[0] - 2,2, self.usertext) #Clear the buffer
        self.addtext(self.username + " $> ",self.size[0] - 2,2, self.usertext)

    def start_chat(self):
        self.drawchat()
        chatline = self.get_input(self.size[0] - 2, len(self.username) + 6,maxsize=160)
        self.NetWrap.sendmessage(chatline.decode("utf-8"))
        self.addmessage(self.username + " -> " + chatline)

    def close(self):
        curses.endwin()

def Establish():
    UI = CurseUI()
    UI.addtext("Nibble's Chat Client - Connecting...", 1, 2, 4)
    x = UI.get_username()
    if UI.connect():
        UI.screen.clear()
        while True:
            UI.start_chat()
    else:
        UI.addtext("Nibble's Chat Client - Connection failed ! Retrying in 10 sec...", 1, 2, 1)
        time.sleep(10)
        Establish()

if __name__ == "__main__":
    Establish()
