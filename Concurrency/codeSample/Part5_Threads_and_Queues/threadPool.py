#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import threading
import time
from queue import Queue


# 创建队列实例，用于存储任务
queue = Queue()


# 定义需要线程池执行的任务
def do_job():
    while True:
        i = queue.get()         # Remove and return an item from the queue.
        time.sleep(1)
        print("index {}, current: {}".format(i, threading.current_thread()))
        queue.task_done()       # Indicate that a formely enqueued task is complete. queue的数据就会减少


if __name__ == '__main__':
    # 创建包括3个线程的线程池
    # 将线程池的线程设置成deamon守护进程，意味着主线程退出时，守护线程也会自动退出，如果使用默认deamon=False，非daemon线程会阻塞
    # 主线程的退出，所以，即使queue队列任务已经完成，线程池依然阻塞无线循环等待任务，使得主线程不会退出
    for i in range(3):
        t = threading.Thread(target=do_job)
        t.daemon = True     #  设置线程daemon 主线程推出， daemon线程也会推出， 即使正在运行，
        t.start()

    # 模拟创建线程池3秒后安排10个任务队列
    time.sleep(3)
    for i in range(10):
        queue.put(i)
    queue.join()            # 主线程设置阻塞，直到任务队列已经清空，解除阻塞

"""
    GIL对线程的影响
        因为python线程虽然时真正的线程，但是解释器执行代码，有一个GIL锁，Global Interpreter Lock.任何Python线程执行前，必须先获取GIL
        锁，然后，每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行，这个GIL全局锁实际上把所有线程的执行代码都给上了锁，所以，
        多线程在Python中只能交替执行，即使100个线程跑在100核心CPU上，也只能用到1个核心。
        
        对于IO密集型任务，多线程还是有很大效率提升，
        
    线程池要设置为多少？
        计算线程数设置的公式？
            N核服务器，执行逻辑单线程本地计算时间X，等待时间Y，工作线程数 = N*（x+y）/ x 
"""