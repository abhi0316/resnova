import socket
c=socket.socket()
host=""
port=12349
c.bind((host,port))
c.listen(1)
a,addr=c.accept()
print "connected form:",addr
a.send("tanks for connecting")	
while True:
	
        print a.recv(1024)
	b= raw_input("enter message>>")
	a.send(b)

