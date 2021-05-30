

import socket
server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(('127.0.0.1',8080))
res = server.recvfrom(1024)
print(res)
res = server.recvfrom(1024)
print(res)
server.close()