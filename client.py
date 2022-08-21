# client

import socket
s = socket.socket()
ip = 'localhost'
port = 9999
s.connect((ip, port))
print('Tilkoblet, velkommen...')

while True:
    print(s.recv(1024).decode())
    msg = input("[YOU] >>> ")
    s.send(msg.encode())
