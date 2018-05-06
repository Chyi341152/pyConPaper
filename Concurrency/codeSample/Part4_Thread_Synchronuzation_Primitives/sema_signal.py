#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# sema_signal.py
#
# An example of using a semaphore for signaling between threads

import threading
import time


done = threading.Semaphore(0)           # Resource control.
item = None

def producer():
    global item
    print("I'm the producer and I produce data.")
    print("Producer is going to sleep.")
    time.sleep(5)
    item = "Hello"
    print("Producer is alive. Signaling the consumer.")
    done.release()                      # Increments the count and signals waiting threads

def consumer():
    print("I'm a consumer and I want for date.")
    print("Consumer is waiting.")
    done.acquire()                      # Waits for the count is 0, otherwise decrements the count and continues
    print("Consumer got", item)


t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)

t1.start()
t2.start()
"""
    Semaphore Uses:
        1. Resource control
            You can limit the number of threads performing certain operations.For example, performing database queries making network connections
        2. Signaling
            Semaphores can be used to send "signals" between threads. For example, having one thread wake up another thread
"""
