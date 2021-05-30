from socket import *
import struct
client = socket(AF_INET,SOCK_STREAM)
client.connect(('127.0.0.1',8081))

while True:
    msg = input('>>>: ').strip()
    if len(msg) == 0: continue
    client.send(msg.encode('utf-8'))

    # 解决粘包
    # 1.拿到数据大小（先收固定长度的头）
    # 2.recv_size = 0,循环接收，recv_size+=接收的长度
    # 3.recv_size == total_size退出循环
    header = client.recv(4)
    total_size = struct.unpack('i',header)[0]
    recv_size = 0
    cmd_res = b''
    while recv_size < total_size:
        recv_data = client.recv(1024)
        recv_size += len(recv_data)
        # cmd_res += recv_data
        print(recv_data.decode('gbk'), end='')
    else:
        print()
    # cmd_res = client.recv(1024) # 本次最大接受1024个字节
    # print(cmd_res.decode('gbk'))

# 粘包问题的原因
# 1.tcp是流式协议，数据黏在一起，=没有便截取部分
# 2.收数据没收干净

# 解决的核心：没次都收干净
