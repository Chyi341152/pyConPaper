#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# event_barrier.py
#
# Using an event to implement a synchronization barrier

import threading
import time


init = threading.Event()            # Resource control.


# This can be used to have one or more threads wait for something to occur
def worker():
    init.wait()                     # Wait for event
    print("I'm worker", threading.current_thread().name)


def initialize():
    print("Initializing some data")
    time.sleep(5)
    print("Unblocking the workers")
    init.set()                      # Set event; Done initializing


# Launch a bunch of worker threads
threading.Thread(target=worker).start()     # Launch workers
threading.Thread(target=worker).start()
threading.Thread(target=worker).start()
threading.Thread(target=worker).start()


# Go initialize and eventually unlock the workers
initialize()                                # Initialize