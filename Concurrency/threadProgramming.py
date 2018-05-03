#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import threading  # --- Thread-based parallelism
import time

# threading module
class CountdownThread(threading.Thread):

    def __init__(self, count):
        threading.Thread.__init__(self)
        self.count = count

    def run(self): # Method representing the thread's activity
        while self.count > 0:
            print("Counting down", self.count)
            self.count -= 1
            time.sleep(1)
        return


# Functions as threads
def countdown(count):
    while count > 0:
        print("Counting down", count)
        count -= 1
        time.sleep(1)


if __name__ == '__main__':
    t1 = CountdownThread(10)    # Create the thread object
    t1.start()                  # Launch the thread

    t2 = CountdownThread(20)    # Create another thread
    t2.start()                  # Launch another thread

    # Create a Thread object, but its run() method just calls the given function
    t3 = threading.Thread(target=countdown, args=(10,))
    t3.start()                  # Launch a thread
    t3.join()                   # Waits for thread t3 to exits, the below "Macintosh 1984" can print

    print("Macintosh 1984")