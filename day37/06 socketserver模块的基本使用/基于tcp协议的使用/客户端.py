from socket import *

client = socket(AF_INET,SOCK_STREAM)
client.connect(('127.0.0.1',8888))

while True:
    msg = input('>>>: ').strip()
    if len(msg) == 0: continue
    client.send(msg.encode('utf-8'))

    # 解决粘包
    # 1.拿到数据大小
    # 2.recv_size = 0,循环接收，recv_size+=接收的长度
    cmd_res = client.recv(1024) # 本次最大接受1024个字节
    print(cmd_res.decode('gbk'))

# 粘包问题的原因
# 1.tcp是流式协议，数据黏在一起，=没有便截取部分
# 2.收数据没收干净

# 解决的核心：没次都收干净
