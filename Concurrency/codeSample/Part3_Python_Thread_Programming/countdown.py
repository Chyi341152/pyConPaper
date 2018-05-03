#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# countdown.py
# An example of defining a thread as a class


import threading  # --- Thread-based parallelism
import time

# threading module
class CountdownThread(threading.Thread):

    def __init__(self, count):
        threading.Thread.__init__(self)
        self.count = count

    def run(self):          # Method representing the thread's activity
        while self.count > 0:
            print("Counting down", self.count)
            self.count -= 1
            time.sleep(1)
        return


# Sample execution
t1 = CountdownThread(10)    # Create the thread object
t2 = CountdownThread(20)

t1.start()                  # Launch the thread
t2.start()