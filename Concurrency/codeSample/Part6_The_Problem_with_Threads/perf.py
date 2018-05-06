#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# perf.py
# A performance problem with threads
import dis              # Disassembler for Python bytecode
import time
import threading


def count(n):           # Consider this CPU-bound function
    while n > 0:
        n -= 1

print(dis.dis(count))

# Sequential Execution
start = time.time()
count(10000000)
count(10000000)
end = time.time()
print("Sequential", end-start)

# Threaded execution
start = time.time()
t1 = threading.Thread(target=count, args=(10000000,))
t2 = threading.Thread(target=count, args=(10000000,))

t1.start()
t2.start()

t1.join()
t2.join()
end = time.time()
print("Threaded  ",end-start)

"""
Sequential 0.951080322265625
Threaded   0.9969501495361328
"""
