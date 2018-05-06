#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# countdownp2.py
# A simple performance test of CPU-bound processes. Compare to the thread example module


import time
import multiprocessing


# Functions as threads
def countdown(count):
    while count > 0:
        count -= 1
    return


start = time.time()
countdown(10000000)
countdown(10000000)
end = time.time()
print("Sequential      ", end-start)


start = time.time()
p1 = multiprocessing.Process(target=countdown, args=(10000000,))     # Create the thread object
p2 = multiprocessing.Process(target=countdown, args=(10000000,))     # Create the thread object

p1.start()                                              # Launch the thread
p2.start()

p1.join()
p2.join()
end = time.time()
print("Multiproceessing", end-start)
print("Macintosh 1984")