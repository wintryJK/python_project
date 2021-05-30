# import queue
from multiprocessing import Queue

# 创建一个队列
q = Queue(5) # 队列存放的数据量

# 存
# q.put(111)

"""
存取数据 存是为了更好的取
"""
q.put(111)
q.put(222)
q.put(333)
q.put(444)
q.put(555)
# q.put(666)

# 队列数据满了之后就会阻塞
v1 = q.get()
v2 = q.get()
v3 = q.get()
v4 = q.get()
v5 = q.get()
# v6 = q.get_nowait() # 没有数据直接报错
# v6 = q.get(timeout=3) # 等3秒报错
# print(v1,v2,v4,v5,v6)
try:
    v6 = q.get(timeout=3)
    print(v6)
except Exception as e:
    print("无")

"""
q.full() # 满？
q.empty() # 空？
q.get_nowait()
在多进程的情况下是不准确的
"""
