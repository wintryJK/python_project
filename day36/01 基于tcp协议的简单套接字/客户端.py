import socket

# 1.买手机
phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # 流式协议=》tcp协议

# 2.拨通电话
phone.connect(("127.0.0.1",8080))

# 3.通信
phone.send('hello jkkkk 哈哈哈'.encode('utf-8'))
data = phone.recv(1024)
print(data.decode('utf-8'))

# 4.关闭连接（必选）
phone.close()