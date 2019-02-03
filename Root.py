#!/usr/bin/python3           # This is server.py file
import socket                                         

# create a socket object
serversocket = socket.socket(
	        socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host  = '127.0.0.2'                           

port = 9993                                     

# bind to the port
serversocket.bind((host, port))                                  

# queue up to 5 requests
serversocket.listen(5)                                           

while True:
    # establish a connection
    clientsocket,addr = serversocket.accept()
    print("Got a connection from %s" % str(addr))
    sitename = clientsocket.recv(2048)
    f=open("dns.txt", "r")
    dnss =f.read()
    namelist = dnss.split(",")
    f.close()
    clientsocket.send(namelist[namelist.index(sitename.decode("ascii"))+1].encode('ascii'))    
    clientsocket.close()
