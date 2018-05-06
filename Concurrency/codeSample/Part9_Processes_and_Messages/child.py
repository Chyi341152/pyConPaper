#!/use/bin/env python3
#-*- coding:utf-8 -*-
# child.py
# A sample child process for receiving messages over a channel

import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import channel


ch = channel.Channel(sys.stdout, sys.stdin)
while True:
    try:
        item = ch.recv()
        ch.send(("child",item))
    except EOFError as e:
        break