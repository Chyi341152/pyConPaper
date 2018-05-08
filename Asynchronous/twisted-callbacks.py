#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from twisted.internet import reactor


def hello():
    reactor.callLater(3, print_hello)


def print_hello():
    print('Hello!')
    reactor.stop()


if __name__ == '__main__':
    reactor.callWhenRunning(hello)
    reactor.run()