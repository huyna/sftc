__author__ = 'HuyNA'
"""
Description
The Server is running at the following address. file
87.107.124.12:25565
87.107.124.12:25565
"""

import os
import socket
import time
import struct
import sys
import base64

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "87.107.124.12"
local_host="192.168.248.172"
port = 25565
s.connect((host, port))

