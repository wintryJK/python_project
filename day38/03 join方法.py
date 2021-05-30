# 第一种
from multiprocessing import Process
import time


def task(name,n):
    print('%s is running'%name)
    time.sleep(n)
    print('%s is over'%name)


if __name__ == '__main__':
    # 1 创建一个对象
    p1 = Process(target=task, args=('jason',1))
    p2 = Process(target=task, args=('egon',2))
    p3 = Process(target=task, args=('tank',3))
    # 容器类型哪怕里面只有1个元素 建议要用逗号隔开
    start_time = time.time()
    p1.start()  # 告诉操作系统帮你创建一个进程  异步
    p2.start()  # 告诉操作系统帮你创建一个进程  异步
    p3.start()  # 告诉操作系统帮你创建一个进程  异步
    p1.join()
    p2.join()
    p3.join()
    print('主',time.time()-start_time)