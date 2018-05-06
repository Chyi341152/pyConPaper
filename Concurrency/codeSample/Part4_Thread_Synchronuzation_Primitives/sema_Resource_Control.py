#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# sema_signal.py
#
# An example of using a semaphore for signaling between threads

import threading
import requests
import time


sema = threading.Semaphore(2)           # Max: 2-threads
URL = 'https://stackoverflow.com'

def fetch_page(url):
    sema.acquire()
    try:
        r = requests.get(url)
        print(threading.current_thread(),r.status_code)
    finally:
        sema.release()

# In this example, only 2 threads can be executing the function at once(If there are more, they will have to wait)
for i in range(10):
    t1 = threading.Thread(target=fetch_page,args=(URL,))
    t1.start()
