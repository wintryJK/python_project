import socket

# 1.买手机
phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # 流式协议=》tcp协议

# 2.绑定手机卡
phone.bind(('127.0.0.1',8080)) # 0-65535, 1024以前的都被系统保留使用

# 3.开机
phone.listen(5) # 5指的是半连接池的大小

# 4.等待电话链接请求
conn,client_addr=phone.accept()
# print(conn)
print(client_addr)

# 5.收/发消息
data = conn.recv(1024) # 最大接受的数据量为1024Bytes
print(data.decode('utf-8'))
conn.send(data.upper())

# 6.关闭电话链接conn
conn.close()

# 7.可选 =》 关机
phone.close()