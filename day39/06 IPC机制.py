from multiprocessing import Queue, Process

"""
研究思路：
    1.主进程跟子进程借助队列通信
    2.子进程跟子进程之间通信
"""

def producer(q):
    q.put('23')
    print('hello')

def comsumer(q):
    print(q.get())

if __name__ == '__main__':
    q = Queue()
    p = Process(target=producer,args=(q,))
    p1 = Process(target=comsumer,args=(q,))
    p.start()
    p1.start()
    # print(q.get())