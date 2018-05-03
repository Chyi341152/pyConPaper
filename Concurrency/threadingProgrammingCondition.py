#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import threading

# Condition Variable
items = []
items_cv = threading.Condition()


def worker():
    init.wait()         # Wait until initialized
    print("worker inited")

def initialize():
    print("initing ... ")
    init.set()         # Done initializing

if __name__ == '__main__':

    # Launch workers
    threading.Thread(target=worker).start()
    threading.Thread(target=worker).start()
    threading.Thread(target=worker).start()

    initialize()            # Initialize 

"""
    cv = threading.Condition([LOCK])
    cv.acquire()        # Acquire the underlying lock 
    cv.release()        # Release the underlying lock 
    cv.wait()           # Wait for condition 
    cv.notify()         # Signal that a condition holds 
    cv.notifyAll()      # Signal all threads waiting.
"""