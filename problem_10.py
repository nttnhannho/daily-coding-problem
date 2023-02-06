"""
[Medium]

This problem was asked by Apple.

Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
"""
import threading
from time import time, sleep


class Scheduler:
    def __init__(self):
        self.fns = []  # tuple of (fn, time)
        t = threading.Thread(target=self.poll)
        t.start()

    def poll(self):
        while True:
            now = time() * 1000
            for fn, due in self.fns:
                if now > due:
                    fn()
            self.fns = [(fn, due) for (fn, due) in self.fns if due > now]
            sleep(0.01)

    def delay(self, f, n):
        self.fns.append((f, time() * 1000 + n))


def func_to_call():
    print("Called at", time())


def main():
    scheduler = Scheduler()
    scheduler.delay(func_to_call, 3000)


if __name__ == "__main__":
    main()
