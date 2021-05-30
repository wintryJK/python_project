# from multiprocessing import Process
# from threading import Thread
# import time
# def task(name):
#     print('%s is running'%name)
#     time.sleep(1)
#     print('%s is over'%name)
#
# # 开启线程不需要在main下执行 但习惯写在main下面
#
# if __name__ == '__main__':
#     t = Thread(target=task,args=('egon',))
#     t.start() # 创建线程的开销非常小，几乎一执行就已经创建了
#     print('主')

from threading import Thread
import time


class MyThread(Thread):
    def __init__(self,name):
        """双下"""
        # 重写别人的方法 不知道有啥 调用父类的方法
        super().__init__()
        self.name = name

    def run(self):
        print('%s is runnning'%self.name)
        time.sleep(1)
        print('over')

if __name__ == '__main__':
    t = MyThread('ssa')
    t.start()
    print('zhu')