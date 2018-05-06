#!/use/bin/env python3
#-*- coding:utf-8 -*-
# channel.py
# An example of setting up a message channel between processes using the subprocess module.
# A minimal object that implements a message channel over a pair of file descriptors (like a pipe)

import pickle       # Python object serialization


class Channel(object):
    def __init__(self, out_f, in_f):
        self.out_f = out_f
        self.in_f = in_f

    def send(self, item):
        pickle.dump(item, self.out_f)       # Serializing an object onto a "file"
        self.out_f.flush()

    def recv(self):
        return pickle.load(self.in_f)       # Unserializing an object from a file,pipe,wrapper around a socket


# Example of using the channel
if __name__ == '__main__':
    import subprocess
    p = subprocess.Popen(['python3','./child.py'],
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE)
    ch = Channel(p.stdin, p.stdout)
    ch.send("Hello World")
    print(ch.recv())
    ch.send(42)
    print(ch.recv())
    ch.send([1,2,3,4,5])
    print(ch.recv())