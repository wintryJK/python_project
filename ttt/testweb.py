# S端
import socket

def make_server(ip, port, app): # 代表server
    sock = socket.socket()
    sock.bind((ip, port))
    sock.listen(5)
    print('Starting development server at http://%s:%s/' %(ip,port))
    while True:
        conn, addr = sock.accept()

        recv_data = conn.recv(1024)
        ll=recv_data.decode('utf-8').split('\r\n')
        head_ll=ll[0].split(' ')
        environ={}
        environ['PATH_INFO']=head_ll[1]
        environ['method']=head_ll[0]

        res = app(environ)

        conn.send(b'HTTP/1.1 200 OK\r\n')
        conn.send(b'Content-Type: text/html\r\n\r\n')
        conn.send(res)

        conn.close()

def app(environ):
    # 处理业务逻辑
    with open('timer.html', 'r', encoding='utf-8') as f:
        data = f.read()

    import time
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    data = data.replace('{{ time }}', now)  # 字符串替换
    return data.encode('utf-8')

if __name__ == '__main__':
    make_server('127.0.0.1', 8008, app) # 在浏览器输入http://127.0.0.1:8008,每次刷新都会看到不同的时间
