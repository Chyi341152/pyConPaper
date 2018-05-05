#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# lock_deadlock.py
#
# An example of write code acquires more than one mutex lock at time

import threading

X = 0  # A shared Value
Y = 0
COUNT = 10000000
# Primarily used to synchronize threads so that only one thread can make modifications to shared data at any given time.
X_Lock = threading.Lock()  # A lock for synchronizing access to X
Y_Lock = threading.Lock()

def addition():
    global X, Y
    for i in range(COUNT):
        X_Lock.acquire()  # Acquire the lock
        # Example critical section
        try:
            X += 1  # Critical Section
            Y_Lock.acquire()
            try:
                Y += 1
            finally:
                Y_Lock.release()
        finally:
            X_Lock.release()  # Release the lock


def subtraction():
    global X, Y
    for i in range(COUNT):
        Y_Lock.acquire()
        try:
            Y -= 1
            X_Lock.acquire()
            try:
                X -= 1
            finally:
                X_Lock.release()
        finally:
            Y_Lock.release()


t1 = threading.Thread(target=subtraction)
t2 = threading.Thread(target=addition)

t1.start()
t2.start()

t1.join()
t2.join()

print(X,Y)

"""
    Only one thread can successfully acquire the lock at any given time 
    If another thread tries to acquire the lock when its already in use. it gets blocked until the lock is released.

"""