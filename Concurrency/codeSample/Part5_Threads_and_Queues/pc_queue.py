#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# pc_queue.py
# An example of using queues to set up producer/consumer problems

import threading
import time
import queue   # Constructor for a FIFO; Python has a thread-safe queuing module

# A queue of items being produced
items = queue.Queue()

# A producer thread
def producer():
    print("I'm the producer")
    for i in range(30):
        items.put(i)            # Put an item on the queue
        time.sleep(1)

# A consumer thread
def consumer():
    print("I'm consumer", threading.current_thread().name)
    while True:
        x = items.get()         # Get an item from the queue
        print(threading.current_thread().name, "got", x)
        time.sleep(1)

# Launch a bunch of consumers
cons = [threading.Thread(target=consumer) for i in range(10)]

for c in cons:
    c.setDaemon(True)
    c.start()


# Run the producer
producer()

"""
    Critical point: You don't need locks here 
    from queue import Queue
    
    q = Queue()     # Create a queue 
    q.put(item)     # Put an item on the queue 
    q.get()         # Get an item from the queue 
    q.empty()       # Check if empty 
    q.full()        # Check if full 
    
    # Queues also have a signaling mechanism 
    q.task_done()   # Signal that work is done 
    q.join()        # Wait for all work to be done 
"""