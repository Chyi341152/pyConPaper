#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import time


# Print "hello", wait three seconds, then print "world"
def hello():
    print("Hello")
    time.sleep(3)
    print("World!")


if __name__ == '__main__':
    hello()