from multiprocessing import Process, Lock
import json
import time
import random

"""
互斥锁：
多个进程操作同一份数据的时候，会出现数据错乱的问题
针对上述问题，加锁，将并发变成串行，牺牲效率保证数据安全
"""
# 查票
def search(i):
    with open('data','r',encoding='utf8') as f:
        dic = json.load(f)
    print('用户%s查询余票：%s'%(i,dic.get('ticket_num')))
    # 字典取值不要用[] 推荐使用get []没有会报错

def buy(i):
    with open('data','r',encoding='utf8') as f:
        dic = json.load(f)
    time.sleep(random.randint(1,3))
    # 判断当前是否有票
    if dic.get('ticket_num') > 0:
        dic['ticket_num']  -= 1
        # 写入数据库
        with open('data', 'w', encoding='utf8') as f:
            json.dump(dic,f)
        print('用户%s买票成功'%i)
    else:
        print('用户%s买票失败'%i)

def run(i, mutex):
    search(i)
    # 给买票环节加锁处理
    # 枪锁
    mutex.acquire()
    buy(i)
    # 释放锁
    mutex.release()

if __name__ == '__main__':
    # 在主进程中生成一把锁，子进程谁先抢到谁先买票
    mutex = Lock()
    for i in range(1,10):
        p = Process(target=run,args=(i,mutex))
        p.start()

"""
拓展  行锁   表锁

注意：
    1.锁不要轻易使用，容易造成死锁，一般用内部封装好的
    2.锁只在处理数据的时候加来保证数据安全，只在争抢数据的时候才用到
"""