#!/usr/bin/python3           # This is client.py file

import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = '127.0.0.2'                          

port = 9993

# connection to hostname on the port.
s.connect((host, port))                               

adres = "smtp.mehmetcan.com"

s.send(adres.encode('ascii'))

ip = s.recv(1024)

print(ip.decode('ascii'))

s.close()
ns = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

more = ip.decode("ascii").split(":")

nhost = more[0]

nport= int(more[1])

ns.connect((nhost, nport))
# Receive no more than 1024 bytes
msg = ns.recv(1024)                                     
typ = 'pop3' 
#s.send(typ)


ns.send(typ.encode('ascii'))


mails = ns.recv(2048)

f=open("istemci_mail.txt", "a+")
f.write(mails.decode('ascii')+ "\r\n")
f.close()

f=open("istemci_mail.txt", "r")
local =f.read()
print(local)

ns.close()

print (msg.decode('ascii'))
