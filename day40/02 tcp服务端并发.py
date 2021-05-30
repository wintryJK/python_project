import socket
from threading import Thread
from multiprocessing import Process

"""
服务端：
    1.要求固定的ip和port
    2.24小时不间断的提供服务
    3.能够支持并发
"""

server = socket.socket() # 括号内不加参数就是tcp
server.bind(('127.0.0.1',8088))
server.listen(5)

# 将服务的代码单独封装成一个函数
def talk(conn):
    while True:
        try:
            data = conn.recv(1024)
            # 针对mac linux 客户端断开连接后
            if len(data) == 0: break
            print(data.decode('utf8'))
            conn.send(data.upper())
        except ConnectionResetError as e:
            print(e)
            break
    conn.close()

# 连接循环
while True:
    conn, addr = server.accept()
    # 服务
    t = Thread(target=talk,args=(conn,))
    t.start()
