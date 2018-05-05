#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# lock_with.py
#
# An example of using a lock with the Python 2.6 context-manager feature

import threading

X = 0  # A shared Value
COUNT = 1000000
# Primarily used to synchronize threads so that only one thread can make modifications to shared data at any given time.
X_Lock = threading.Lock()  # A lock for synchronizing access to X


def addition():
    global X
    for i in range(COUNT):
        with X_Lock:        # This automatically acquires the lock and releases it when control enters/exits the associated block of statements
            X += 1


def subtraction():
    global X
    for i in range(COUNT):
        with X_Lock:
            X -= 1


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