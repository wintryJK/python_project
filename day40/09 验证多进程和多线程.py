# 计算密集型
from multiprocessing import Process
from threading import Thread
import os,time

# def work():
#     res = 1
#     for i in range(1,20000):
#         res *= i
#
# if __name__ == '__main__':
#     l = []
#     print(os.cpu_count())
#     start_time = time.time()
#     for i in range(12):
#         p = Thread(target=work)
#         p.start()
#         l.append(p)
#     for p in l:
#         p.join()
#     print(time.time()-start_time)

# IO密集型
def work():
    time.sleep(1)

if __name__ == '__main__':
    l = []
    print(os.cpu_count())
    start_time = time.time()
    for i in range(100):
        p = Process(target=work)
        p.start()
        l.append(p)
    for p in l:
        p.join()
    print(time.time()-start_time)

"""
总结：
多进程和多线程都有各自的优势
一半都是多进程+多线程

"""
