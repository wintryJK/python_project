

"""
生产者：生产/制造
消费者：消费/处理
还需要一个媒介
    生产者和消费者之间不是直接交互的

生产者 + 消息队列 + 消费者
"""

from multiprocessing import Process, Queue, JoinableQueue
import time
import random

def producer(name,food,q):
    for i in range(5):
        data = '%s生产了%s%s'%(name,food,i)
        time.sleep(random.randint(1,3))
        print(data)
        q.put(data)

def comsumer(name,q):
    while True:
        food = q.get()
        # if food is None:
        #     break
        time.sleep(random.randint(1,3))
        print("%s吃了%s"%(name,food))
        q.task_done()

if __name__ == '__main__':
    # q = Queue()
    q = JoinableQueue()
    p1 = Process(target=producer,args=('大厨','包子',q))
    p2 = Process(target=producer,args=('tt','水',q))
    c1 = Process(target=comsumer,args=('aa',q))
    c2 = Process(target=comsumer,args=('bb',q))
    p1.start()
    p2.start()
    c1.daemon = True
    c2.daemon = True
    c1.start()
    c2.start()
    p1.join()
    p2.join()
    # q.put(None) # 肯定在所有生产者
    # q.put(None) # 肯定在所有生产者
    q.join() # 等待队列中所有的数据都被取完再往下执行代码
    """
    JoinableQueue 内部有计数器， 存数据+1 
    调用task_done 计数器-1
    q.join() 当计数器为0时 才往后运行
    """
    # 只要q.join执行完 消费者已经处理完毕数据了 消费者没有存在的必要了
