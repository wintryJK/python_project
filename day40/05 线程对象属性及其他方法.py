from threading import Thread, active_count, current_thread
import os
import time

def task(n):
    # print('aaa',os.getpid())
    print('aaa',current_thread().name)
    time.sleep(n)

if __name__ == '__main__':
    t = Thread(target=task,args=(1,))
    t1 = Thread(target=task,args=(2,))
    t.start()
    t1.start()
    t.join()
    print('主',active_count()) # 统计当前活跃的线程数
    # print('主',current_thread().name) # 获取线程的名字