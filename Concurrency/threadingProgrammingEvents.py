#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import threading

e = threading.Event()



if __name__ == '__main__':
    limitResource() # Using a semaphore to limit resources
    producerConsumer() #
