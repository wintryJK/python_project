from socket import *
import subprocess

server = socket(AF_INET,SOCK_STREAM)
server.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
server.bind(('127.0.0.1',8081))
server.listen(5)

# 服务端应该做的两件事
# 1.循环从半连接池中取出请求与其建立双向连接，拿到连接对象
while True:
    conn,client_addr = server.accept()

    # 2.拿到连接对象，循环通信
    while True:
        try:
            msg = conn.recv(1024)
            if len(msg) == 0 : break
            conn.send(msg.upper())
        except Exception:
            break
    conn.close()
