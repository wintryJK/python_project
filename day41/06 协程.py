"""
进程：资源单位
线程：执行单位
协程：这个概念是程序员自己提出来的
    单线程下实现并发
    程序员自己在代码层面上监控IO操作
    遇到IO 在代码级别完成切换
    给cpu的感觉是程序一直在运行 没有IO
    提升程序的运行效率

多道技术：
    切换+保存状态
    cpu两种切换
        1.遇到IO
        2.程序长时间占用

TCP服务端
    accept
    recv
代码如何做到切换加保存状态
切换：
    切换不一定是提升效率，也有可能是降低效率
    IO切 -- 提升
    没有IO -- 降低
保存状态：
    yield
"""

import time

# def func1():
#     for i in range(1000000):
#         i + 1
#
# def func2():
#     for i in range(1000000):
#         i + 1
#
# start_time = time.time()
# func1()
# func2()
# print(time.time()-start_time)

# def func1():
#     while True:
#         1000000+1
#         yield
#
# def func2():
#     g = func1()  # 先初始化生成器
#     for i in range(1000000):
#         i + 1
#         next(g)
#
# start_time = time.time()
# # func1()
# func2()
# print(time.time()-start_time)