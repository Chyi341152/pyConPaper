#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# event_notify.py
# Using an event and semaphore to implement a kind of notification mechanism
# An example of using a semaphore and an event to have a thread
# signal completion of some task

import threading
import time


# A variable that contains some data
item = None

# A semaphore to indicate that an item is available
available = threading.Semaphore(0)

# An event to indicate that processing is complete
completed = threading.Event()


# A worker thread
def worker():
    while True:
        available.acquire()
        print("worker: processing", item)
        time.sleep(5)
        print("worker: done")
        completed.set()


# A producer thread
def producer():
    global item
    for x in range(5):
        completed.clear()       # Clear the event
        item = x                # Set the item
        print("producer: produced an item")
        available.release()     # Signal on the semaphore
        completed.wait()        # wait until
        print("producer: item was processed")


t1 = threading.Thread(target=producer)
t1.start()
t2 = threading.Thread(target=worker)
t2.setDaemon(True)
t2.start()