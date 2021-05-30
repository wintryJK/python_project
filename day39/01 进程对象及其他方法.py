from multiprocessing import Process, current_process
import time
import os


def task():
    # 一台计算机用pid区分进程服务，进程号
    # windows tasklist |findstr PID
    print('%s is running' % current_process().pid)
    # print('%s 子进程的主进程号' % os.getppid())
    time.sleep(30)

if __name__ == '__main__':
    p = Process(target=task)
    # p.daemon = True # 将进程p设置成守护进程，放在start上面
    p.start()
    # p.terminate() # 杀死当前进程
    # 告诉操作系统杀死当前进程 但是需要一点时间
    # time.sleep(0.1)
    # print(p.is_alive()) # 当前进程是否存活
    """
    一般情况下，
    存储布尔值的变量名 和 返回结果是布尔值的方法名
    都起成is_开头
    """
    print('主',current_process().pid)
    # print('主',os.getpid())
    # print('主主',os.getppid()) # 查看当前进程的父进程号


