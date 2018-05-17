#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
    Dining philosophers
        Five philosophers, Aristotle亚里士多德,Kant康德,Spinoza斯宾诺莎,Marx马克思 and Russell罗素(the tasks) spend their time thinking and eating spaghetti.
        They eat at a round table with five individual seats. For eating each philosopher needs two forks.When a philosopher cannot grab both forks it sits and waits.
        Eating takes random time, then the philosopher puts the forks down and leaves the dining room, After spending some random time thinking about the nature of the universe
        he again becomes hungry, and the circle repeats itself.
"""
import threading
import random
import time

# Dining philosophers, 5 Phillies with 5 forks. Must have two forks to eat.
#
# Deadlock is avoided by never waiting for a fork while holding a fork (locked)
# Procedure is to do block while waiting to get first fork, and a nonblocking
# acquire of second fork. If failed to get second forks, release first fork
# swap which fork is first and which is second and retry until getting both
#
# See discustion page note about 'live lock'.

class Philosopher(threading.Thread):

    running = True

    def __init__(self, xname, forkOnLeft, forkOnRight):
        threading.Thread.__init__(self)
        self.name = xname
        self.forkOnLeft = forkOnLeft
        self.forkOnRight = forkOnRight

    def run(self):
        while(self.running):
            # Philosopher is thinking (but realy is sleeping)
            time.sleep(random.uniform(3,13))
            print('[%s] is hungry.' % self.name)
            self.dine()

    def dine(self):
        fork1, fork2 = self.forkOnLeft, self.forkOnRight

        while self.running:
            fork1.acquire(blocking=True)                    # Acquire a lock, blocking
            locked = fork2.acquire(blocking=False)          # Acquire a lock, non-blocking
            if locked: break
            fork1.release()
            print('[%s] swap forks' % self.name)
            fork1, fork2 = fork2, fork1
        else:                                               # the else clause is only executed when your while condition becomes false.
            return                                          # If break out of the loop, or if an exception is raised, it won't be executed
        self.dining()
        fork2.release()
        fork1.release()

    def dining(self):
        print('[%s] starts eating' % self.name)
        time.sleep(random.uniform(1,10))
        print("[%s] finishes eating and leaves to think." % self.name)

def DiningPhilosophers():
    forks = [threading.Lock() for n in range(5)]
    philosopherNames = ('Aristotle', '  Kant   ', ' Buddha  ', '  Marx   ', ' Russel  ')

    philosophers = [Philosopher(philosopherNames[i], forks[i%5], forks[(i+1)%5]) for i in range(5)]

    random.seed(158968)
    Philosopher.running = True
    for p in philosophers:
        p.start()

    time.sleep(120000)
    Philosopher.running = False
    print("Now we're finishing.")


if __name__ == '__main__':
    DiningPhilosophers()