#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# countdown2.py
# Launching a function into a separate thread


import threading  # --- Thread-based parallelism
import time


# Functions as threads
def countdown(count):
    while count > 0 :
        print("Counting down", count)
        count -= 1
        time.sleep(1)
    return


# Sample execution
t1 = threading.Thread(target=countdown, args=(10,))     # Create the thread object
t1.start()                                              # Launch the thread
t1.join()                                               # Waits for thread t1 to exit 

print("Macintosh 1984")                                 # Test t1.join() wait for