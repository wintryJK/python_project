from gevent import spawn
from gevent import monkey
monkey.patch_all()
"""
gevent本身无法检测一些常见的IO操作
from gevent import monkey
monkey.patch_all()
上面两句话必导入
"""
import time

def heng():
    print('heng')
    time.sleep(2)
    print('heng')

def ha():
    print('ha')
    time.sleep(3)
    print('ha')

start_time = time.time()
g1 = spawn(heng)
g2 = spawn(ha)
g1.join()
g2.join()
print(time.time()-start_time)

"""
总结：单线程也可以实现
多进程下开设多线程
多线程下面开启协程
从而使执行效率提升
"""