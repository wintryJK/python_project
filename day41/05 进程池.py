"""
池是用来保证计算机安全的情况下最大限度的利用计算机
降低了运行效率，但是保证了计算机的硬件安全
"""
import os
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
import time


# pool = ThreadPoolExecutor(5) # 池子里面固定只有五个线程
# 括号内可以传数字，默认计算机cpu个数*5
pool = ProcessPoolExecutor(5) # 五个进程
# 括号内可以传数字，默认计算机cpu个数

"""
创造出来的线程/进程不会出现重复创建和销毁的过程
使用：只需将任务提交
任务的提交方式：
    同步：提交任务原地等待返回结果
    异步：不等待任务的返回结果
        异步提交的返回结果 应该通过回调机制来获取
        
"""
def task(n):
    print(n,os.getpid())
    time.sleep(2)
    return n**n
def call_back(n):
    print('call_back>>>: ',n.result())
if __name__ == '__main__':

    t_list = []
    for i in range(12):
        res = pool.submit(task,i).add_done_callback(call_back) # 朝池中提交任务
        t_list.append(res) # result  同步提交  join
    # 等待池中所有的任务执行完毕再往下执行
    # pool.shutdown() # 关闭线程池 等待线程池所有任务执行完毕
    # for t in t_list:
    #     print('>>>: ',t.result())
"""
由并发变成了串行
"""

