#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# rlock_ex.py
#
# An example of using a reentrant lock . Every method of the class
# below uses the same RLock object, However, some methods cal
# other methods. There nested calls will work within the same thread

import threading

class Foo(object):
    lock = threading.RLock()

    def __init__(self):
        self.x = 0

    def add(self,n):
        with Foo.lock:
            self.x += n

    def incr(self):
        with Foo.lock:
            self.add(1)

    def decr(self):
        with Foo.lock:
            self.add(-1)


# Two functions that will run in separate threads and call methods
# on the above class.
def adder(f, count):
    while count > 0:
        f.incr()
        count -= 1

def subber(f, count):
    while count > 0:
        f.decr()
        count -= 1


# Create some threads and make sure it works
COUNT = 100000
f = Foo()

t1 = threading.Thread(target=adder, args=(f, COUNT))
t2 = threading.Thread(target=subber, args=(f, COUNT))

t1.start()
t2.start()

t1.join()
t2.join()

print(f.x)

"""
    Only one thread can successfully acquire the lock at any given time 
    If another thread tries to acquire the lock when its already in use. it gets blocked until the lock is released.

"""