#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import threading
import requests


URL = 'https://stackoverflow.com'

done = threading.Semaphore(0)
sema = threading.Semaphore(2)          # Max: 5-threads
# A counter-based synchronization primitive
# acquire() - Waits if the count is 0, otherwise decrements the count and continues
# release() - Increments the count and signals waiting threads
# acquire()/release() can be called in any order and by any thread

def fetch_page(url):
    sema.acquire()
    try:
        r = requests.get(url)
        print(r.status_code)
    finally:
        sema.release()

def limitResource():
    t1 = threading.Thread(target=fetch_page, args=(URL,))
    t2 = threading.Thread(target=fetch_page, args=(URL,))
    t3 = threading.Thread(target=fetch_page, args=(URL,))
    t4 = threading.Thread(target=fetch_page, args=(URL,))
    t5 = threading.Thread(target=fetch_page, args=(URL,))
    t6 = threading.Thread(target=fetch_page, args=(URL,))
    t7 = threading.Thread(target=fetch_page, args=(URL,))
    t8 = threading.Thread(target=fetch_page, args=(URL,))
    t9 = threading.Thread(target=fetch_page, args=(URL,))
    t10 = threading.Thread(target=fetch_page, args=(URL,))
    t11 = threading.Thread(target=fetch_page, args=(URL,))
    t12 = threading.Thread(target=fetch_page, args=(URL,))

    t1.start();t2.start();t3.start();t4.start();t5.start();t6.start();t7.start()
    t8.start();t9.start();t10.start();t11.start();t12.start()

    t1.join();t2.join();t3.join();t4.join();t5.join();t6.join()
    t7.join();t8.join();t9.join();t10.join();t11.join();t12.join()

def producer():
    try:
        print('This is Producer: ')
    finally:
        done.release()

def consumer():
    try:
        done.acquire()
        print('This is consumer:')
    finally:
        pass

def producerConsumer():
    p1 = threading.Thread(target=producer)
    c1 = threading.Thread(target=consumer)
    p1.start();c1.start()
    p1.join();c1.join()

if __name__ == '__main__':
    limitResource() # Using a semaphore to limit resources
    producerConsumer() #
