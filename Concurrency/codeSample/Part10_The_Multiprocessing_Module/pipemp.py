#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# pipemp.py
# An example of a multiprocessing producer/consumer with a pipe

import multiprocessing


def consumer(p1, p2):
    p1.close()              # Close producer's end
    while True:
        try:
            item = p2.recv()
        except EOFError:
            break
        print(item)         # Do other useful work here


def producer(sequence, output_p):
    for item in sequence:
        output_p.send(item)


if __name__ == '__main__':
    p1, p2 = multiprocessing.Pipe()                 # A channel for sending/receiving objects
    cons = multiprocessing.Process(target=consumer,
                                   args=(p1,p2))
    cons.start()

    # Close the input end in the producer
    p2.close()

    # Go produce some data
    sequence = range(100)   # Replace with useful data
    producer(sequence, p1)

    # Close the pipe
    p1.close()

