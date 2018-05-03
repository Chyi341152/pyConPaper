#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import threading

X = 0           # A shared values
X_lock = threading.Lock()

def foo():
    global  X
    for i in range(1000000):
        # Automatically acquires the lock and releases it when control enters/exits the associated block of statements
        with X_lock:
            X += 1

def bar():
    global X
    for i in range(1000000):
        # Automatically acquires the lock and releases it when control enters/exits the associated block of statements
        with X_lock:
            X -= 1

if __name__ == '__main__':
    t1 = threading.Thread(target=foo)
    t2 = threading.Thread(target=bar)

    t1.start(); t2.start()
    t1.join(); t2.join()                # Wait for completion
    print(X)                            # Expected result is 0
