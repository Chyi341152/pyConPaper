#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# lock_ex.py
#
# An example of using a lock to synchronize access to shared data

import threading

X = 0                       # A shared Value
COUNT = 1000000
# Primarily used to synchronize threads so that only one thread can make modifications to shared data at any given time.
X_Lock = threading.Lock()   # A lock for synchronizing access to X

def addition():
    global X
    for i in range(COUNT):
        X_Lock.acquire()        # Acquire the lock
        # Example critical section
        try:
            X += 1                  # Critical Section
        finally:
            X_Lock.release()        # Release the lock

def subtraction():
    global X
    for i in range(COUNT):
        X_Lock.acquire()
        try:
            X -= 1
        finally:
            X_Lock.release()


t1 = threading.Thread(target=subtraction)
t2 = threading.Thread(target=addition)

t1.start()
t2.start()

t1.join()
t2.join()

print(X)

"""
    Only one thread can successfully acquire the lock at any given time 
    If another thread tries to acquire the lock when its already in use. it gets blocked until the lock is released.
    
"""