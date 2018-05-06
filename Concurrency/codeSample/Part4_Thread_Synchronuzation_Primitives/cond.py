#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# cond.py
# An example of using a condition variable to set up a producer/consumer problem


import threading
import time


# A list of items that are being produced. Note: It is actually
# more efficient to use a collections.deque() object for this.
items = []

# A condition veriable for items
items_cv = threading.Condition()


# A producer thread
def producer():
    print("I'm the producer")
    for i in range(30):
        with items_cv:                  # Always must acquire the lock first
            items.append(i)             # Add an item to the list
            items_cv.notify()           # Send a notification signal
        time.sleep(1)


# A consumer thread
def consumer():
    print("I'm a consumer %s" % threading.current_thread().name)
    while True:
        with items_cv:                  # Must always acquire the lock
            while not items:            # Check if there are any items
                items_cv.wait()         # if not, we have to sleep
            x = items.pop(0)            # Pop an item off
        print(threading.current_thread().name,"got",x)
        time.sleep(5)


# Launch a bunch of consumers
cons = [threading.Thread(target=consumer) for i in range(10)]

for c in cons:
    c.setDaemon(True)
    c.start()

# Run the producer
producer()