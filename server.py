# server

import socket

s = socket.socket()
ip = 'localhost'
port = 9999
s.bind((ip, port))
s.listen()
print('wait for client')
c, add = s.accept()
print("client added ")
while True:
    msg = input("[YOU] >>> ")
    c.send(msg.encode())
    print(c.recv(1024).decode())
