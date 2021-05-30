from threading import Thread
import time

# def task(name):
#     print('%s is running'%name)
#     time.sleep(1)
#     print('over')
#
# if __name__ == '__main__':
#     t = Thread(target=task,args=('aa',))
#     t.daemon = True
#     t.start()
#     print("主")

"""
主线程运行结束之后不会立即结束，会等待其他非守护线程结束之后才会结束
主线程结束意味着所在进程的结束
"""
from multiprocessing import Process

def foo():
    print(123)
    time.sleep(1)
    print('end123')

def func():
    print(456)
    time.sleep(3)
    print('end456')

if __name__ == '__main__':
    t1 = Thread(target=foo)
    t2 = Thread(target=func)
    t1.daemon = True
    t1.start()
    t2.start()
    print('主。。。。。')