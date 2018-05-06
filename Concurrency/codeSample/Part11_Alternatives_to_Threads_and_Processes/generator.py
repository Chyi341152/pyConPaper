#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# generator.py
# A very simple example of using generators to implement a  form of cooperative multitasking


def countdown_task(n):
    while n > 0:
        print(n)
        yield
        n -= 1


# A list of tasks to run
from collections import deque  # list-like container with fast appends and pops on either end


tasks = deque([
    countdown_task(5),          # Each task is a generator function
    countdown_task(10),
    countdown_task(15)
])


def scheduler(tasks):
    while tasks:
        task = tasks.popleft()
        try:
            next(task)              # Run to the next yield
            tasks.append(task)      # Reschedule
        except StopIteration:
            pass

# Run it
scheduler(tasks)