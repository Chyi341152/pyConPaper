#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# race.py
# A simple example of a race condition


import threading  # --- Thread-based parallelism

x = 0   # A shared value
COUNT = 1000000

def addition():
    global x
    for i in range(COUNT):
        x += 1

def subtraction():
    global x
    for i in range(COUNT):
        x -= 1


# Sample execution
t1 = threading.Thread(target=addition)                  # Create the thread object
t2 = threading.Thread(target=subtraction)

t1.start()                                              # Launch the thread
t2.start()

t1.join()                                               # Waits for thread t1 to exit
t2.join()

print(x)                                                # Expected result is 0
print("Macintosh 1984")                                 # Test t1.join() wait for