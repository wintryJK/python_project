
import socket

# 1.买手机
server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # 数据报协议=》udp协议

# 2.绑定手机卡
server.bind(('127.0.0.1',8081)) # 0-65535, 1024以前的都被系统保留使用

while True:
    data,client_addr = server.recvfrom(1024)
    print(data)
    server.sendto(data.upper(),client_addr)

server.close()