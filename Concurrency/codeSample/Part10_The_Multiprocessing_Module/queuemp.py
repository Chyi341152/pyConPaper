#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# queuemp.py
# Using multiprocessing queues with multiprocessing


# A consumer process
def consumer(input_q):
    while True:
        # Get an item from the queue
        item = input_q.get()            # Get an item from the queue
        # Process item
        print(item)
        # Signal completion
        input_q.task_done()             # Signal task completion


# A producer process 
def producer(sequence, output_q):
    for item in sequence:
        # Put the item on the queue
        output_q.put(item)              # Put an item on the queue


if __name__ == '__main__':
    from multiprocessing import Process, JoinableQueue
    q = JoinableQueue()

    # Launch the consumer process
    cons_p = Process(target=consumer, args=(q,))
    cons_p.daemon = True
    cons_p.start()

    # Run the producer function on some data
    sequence = range(100)       # Replace with useful data
    producer(sequence,q)

    # Wait for the consumer to finish
    q.join()                    # Wait for completion