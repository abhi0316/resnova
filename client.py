import socket
c=socket.socket()
host=socket.gethostname()
port=12349
c.connect((host,port))
while True:

	
	print (c.recv(1024))
	a =raw_input ("enter message>>")
	c.send(a)


