#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import threading

X = 0           # A shared values
Y = 0
X_lock = threading.Lock()
Y_lock = threading.Lock()

def foo():
    global  X, Y
    for i in range(1000000):
        # Automatically acquires the lock and releases it when control enters/exits the associated block of statements
        with X_lock:
            X += 1
            with Y_lock:
                Y -= 1

def bar():
    global X, Y
    for i in range(1000000):
        # Automatically acquires the lock and releases it when control enters/exits the associated block of statements
        with Y_lock:
            Y += 1
            with X_lock:
                X -= 1

if __name__ == '__main__':
    t1 = threading.Thread(target=foo)
    t2 = threading.Thread(target=bar)

    t1.start(); t2.start()
    t1.join(); t2.join()                # Wait for completion
    print(X,Y)                            # Expected result is 0
