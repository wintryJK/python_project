from threading import Thread, Lock
import time

mutex = Lock()
money = 100

def task():
    global money
    # mutex.acquire()
    with mutex: # 山下文管理
        tmp = money
        time.sleep(0.1)
        money = tmp - 1
    # mutex.release()

if __name__ == '__main__':

    t_list = []
    for i in range(100):
        t = Thread(target=task)
        t.start()
        t_list.append(t)
    for t in t_list:
        t.join()
    print(money)

"""
100线程刚起来，先抢GIL
进入IO，GIL自动释放，但是互斥锁没有放掉
其他线程虽然抢到了GIL，但是还有互斥锁
最终GIL还是回到自己手上
"""