#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import threading

init = threading.Event()

def worker():
    init.wait()         # Wait until initialized
    print("worker inited")

def initialize():
    print("initing ... ")
    init.set()         # Done initializing

if __name__ == '__main__':

    # Launch workers
    threading.Thread(target=worker).start()
    threading.Thread(target=worker).start()
    threading.Thread(target=worker).start()

    initialize()            # Initialize
