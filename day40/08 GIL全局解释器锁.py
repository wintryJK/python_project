'''
定义：
In CPython, the global interpreter lock, or GIL, is a mutex that prevents multiple
native threads from executing Python bytecodes at once. This lock is necessary mainly
because CPython’s memory management is not thread-safe. (However, since the GIL
exists, other features have grown to depend on the guarantees that it enforces.)
'''

"""
python解释器其实有多个版本
    Cpython
    Jpython
    Pypypython
普遍使用Cpython
在cpython中，GIL用来组织同一个进程下多个线程同时执行
同一个进程下的多个线程无法利用多核优势！！！
因为cpython的内存管理不是线程安全的
内存管理（垃圾回收）
    1.引用计数
    2.标记清楚
    3.分代回收
"""

"""
重点：
    1.GIL不是python的特点而是Cpython的特点
    2.GIL是保证解释器级别的数据的安全
    3.同一个进程下的多个线程无法利用多核优势
    4.针对不同的数据还是需要加不同的锁处理
    5.解释型语言的通病
"""

"""
多线程是否有用要看具体情况
单核：四个任务（IO密集型/计算密集型）
多核：四个任务（IO密集型/计算密集型）
# 计算密集型  每个任务都需要10s
单核：
    多进程：消耗资源
    多线程：好
多核：
    多进程：10
    多线程：40
# IO密集型
多核：
    多进程：相对浪费资源
    多线程：更加节省资源


"""