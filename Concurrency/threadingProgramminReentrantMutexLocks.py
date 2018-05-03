#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import threading

class Foo(object):
    lock = threading.RLock() # A reentrant lock is a synchronization primitive that may be acquired multiple times by the same thread.

    # Only one thread is allowed to execute methods in the class at any given time
    def bar(self):
        with Foo.lock:
            pass

    def spam(self):
        with Foo.lock:
            pass

if __name__ == '__main__':
    t1 = threading.Thread(target=foo)
    t2 = threading.Thread(target=bar)

    t1.start(); t2.start()
    t1.join(); t2.join()                # Wait for completion
    print(X,Y)                            # Expected result is 0
