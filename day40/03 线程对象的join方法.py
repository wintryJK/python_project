from threading import Thread
import time

def task(name):
    print('%s is running'%name)
    time.sleep(3)
    print('%s is over'%name)

if __name__ == '__main__':
    t = Thread(target=task,args=('aa',))
    t.start()
    t.join() # 主线程等待子线程结束再运行
    print('主')