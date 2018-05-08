#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import asyncio

loop = asyncio.get_event_loop()


async def hello():
    print("Hello")
    await asyncio.sleep(3)      # wait for the suspension and assuming
    print('World!')


if __name__ == '__main__':
    loop.run_until_complete(hello())