import socketserver

class MyRequestHandle(socketserver.BaseRequestHandler):
    def handle(self):
        print(self.request) # tcp ==> self.request -> conn
        print(self.client_address)
        while True:
            try:
                msg = self.request.recv(1024)
                if len(msg) == 0: break
                self.request.send(msg.upper())
            except Exception:
                break
            self.request.close()


s = socketserver.ThreadingTCPServer(('127.0.0.1',8888),MyRequestHandle)
s.serve_forever()
# 等同于 循环 accept
# while True:
#   conn,client_addr = server.accept()
#   启动一个线程（conn,client_addr）

# 第二件事：拿到链接对象，与其进行通信循环==》handle方法