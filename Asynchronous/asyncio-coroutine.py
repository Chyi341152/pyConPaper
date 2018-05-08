#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import asyncio      # Asynchronous I/O, event loop coroutines and tasks

loop = asyncio.get_event_loop()


@asyncio.coroutine
def hello():
    print("Hello")
    yield from asyncio.sleep(3)         # suspension suspending a function
    print('World!')


if __name__ == '__main__':
    loop.run_until_complete(hello())