#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# Dining philosophers problem 哲学家就餐问题
# Parallel solution to the dining-philosophers probelm in Python using the threading module
# This is a very simple example of using the threading module to create parallel programs in Python.
# It demonstrates basic locking functions and how to create a custom semaphore to manage concurrent threads.

# Symmetric solution to the "dining philosophers"
# problem. Uses a semaphore as the "butler" to avoid
# deadlock.
import sys
import time
import threading


class Semaphore(object):

    def __init__(self, initial):
        # A condition variable allows one or more threads to wait until they are notified by another thread.
        self.lock = threading.Condition(threading.Lock())
        self.value = initial

    def up(self):
        with self.lock:
            self.value += 1
            self.lock.notify()

    def down(self):
        with self.lock:
            while self.value == 0:
                self.lock.wait()
            self.value -= 1


class ChopStick(object):

    def __init__(self, number):
        self.number = number            # chop stick ID
        self.user = -1                  # keep track of philosopher using it
        self.lock = threading.Condition(threading.Lock())
        self.taken = False

    def take(self, user):               # used for synchronization
        with self.lock:
            while self.taken == True:
                self.lock.wait()
            self.user = user
            self.taken = True
            sys.stdout.write("p[%s] took c[%s]\n" % (user, self.number))
            self.lock.notifyAll()

    def drop(self, user):               # used for synchronization
        with self.lock:
            while self.taken == False:
                self.lock.wait()
            self.user = -1
            self.taken = False
            sys.stdout.write("p[%s] dropped c[%s]\n" %(user, self.number))
            self.lock.notifyAll()


class Philosopher(threading.Thread):

    def __init__(self, number, left, right, butler):
        threading.Thread.__init__(self)
        self.number = number            # Philosopher number
        self.left = left
        self.right = right
        self.butler = butler

    def run(self):
        for i in range(20):
            self.butler.down()          # start service by butler
            time.sleep(0.1)             # think
            self.left.take(self.number) # pickup left chopstick
            time.sleep(0.1)             # yield makes deadlock more likely
            self.right.take(self.number)# pickup right chopstick
            time.sleep(0.1)             # eat
            self.right.drop(self.number)# drop right chopstick
            self.left.drop(self.number) # drop left chopstick
            self.butler.up()            # end service by butler
        sys.stdout.write("p[%s] finished thinking and eating\n" % self.number)


def main():
    # number of philosophers / chop sticks
    n = 5

    # butler for deadlock avoidance (n-1 available)
    butler = Semaphore(n-1)

    # list of chopsticks
    c = [ChopStick(i) for i in range(n)]

    # list of philsophers
    p = [Philosopher(i, c[i], c[(i+1)%n], butler) for i in range(n)]

    for i in range(n):
        p[i].start()


if __name__ == '__main__':
    main()