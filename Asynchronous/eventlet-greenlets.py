#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from eventlet import sleep


def hello():
    print("Hello")
    sleep(3)
    print("World!")


if __name__ == '__main__':
    hello()