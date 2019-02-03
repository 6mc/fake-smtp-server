#!/usr/bin/python3           # This is server.py file
import socket                                         

# create a socket object
serversocket = socket.socket(
	        socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = '127.0.0.3'                           

port = 9992                                           

# bind to the port
serversocket.bind((host, port))                                  

# queue up to 5 requests
serversocket.listen(5)                                           

while True:
    # establish a connection
    clientsocket,addr = serversocket.accept()      

    print("Got a connection from %s" % str(addr))
    
    msg='Thank you for connecting'+ "\r\n"
    clientsocket.send(msg.encode('ascii'))
    istm = clientsocket.recv(2048)
    if istm.decode('ascii')=='pop3':
       f=open("sunucu_mail.txt", "r")
       mails =f.read()
       clientsocket.send(mails.encode('ascii'))
       f.close() 
       f=open("sunucu_mail.txt","w")
       f.write(" ")
       f.close()
    else:
       f=open("sunucu_mail.txt", "r")
       mails =f.read()
       clientsocket.send(mails.encode('ascii'))   
    clientsocket.close()
