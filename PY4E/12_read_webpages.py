#   An HTTP Request in Python

import socket

mysock =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('http://en.wikipedia.org', 80))

cmd = 'GET http://en.wikipedia.org/wiki/Main_Page HTTP/1.0\n\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()