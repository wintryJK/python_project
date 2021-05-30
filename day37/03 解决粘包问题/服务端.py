from socket import *
import subprocess
import struct

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
            cmd = conn.recv(1024)
            if len(cmd) == 0 : break
            obj = subprocess.Popen(cmd.decode('utf-8'),
                             shell=True,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE
                             )
            stdout_res = obj.stdout.read()
            stderr_res = obj.stderr.read()
            total_size = len(stderr_res) + len(stdout_res)
            # 1.先发头信息（固定长度的字节）
            # int -》 固定长度
            header = struct.pack('i',total_size)
            conn.send(header)
            # 2.再发真实的数据
            conn.send(stdout_res+stderr_res) # ???
        except Exception:
            break
    conn.close()
