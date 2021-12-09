"""
[Easy]

This problem was asked by Twitter.

You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to
accomplish this, with the following API:

record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
You should be as efficient with time and space as possible.
"""


class Log:
    def __init__(self, capa):
        self.capa = capa
        self._log = []
        self._cur = 0

    def __str__(self):
        return f"{[record for record in self._log]}"

    def record(self, order_id):
        if len(self._log) >= self.capa:
            self._log[self._cur] = order_id
        else:
            self._log.append(order_id)
        self._cur = (self._cur + 1) % self.capa

    def get_last(self, i):
        if i > len(self._log):
            return "No data"
        return self._log[self._cur - i]


if __name__ == "__main__":
    log = Log(5)  # Initialize log with size = 5

    print("After adding 1, 2, 3")
    # Add records 1, 2, 3 to log => Log = [1, 2, 3]
    log.record(1)
    log.record(2)
    log.record(3)
    print(log)

    for i in range(1, 6):
        print(f"Index {i}th: {log.get_last(i)}")

    print("After adding 4")
    # Add records 4 to log => Log = [1, 2, 3, 4]
    log.record(4)
    print(log)

    for i in range(1, 6):
        print(f"Index {i}th: {log.get_last(i)}")

    print("After adding 5")
    # Add records 5 to log => Log = [1, 2, 3, 4, 5]
    log.record(5)
    print(log)

    for i in range(1, 6):
        print(f"Index {i}th: {log.get_last(i)}")

    print("After adding 6, 7")
    # Add records 6, 7 to log => Log = [6, 7, 3, 4, 5]
    log.record(6)
    log.record(7)
    print(log)

    for i in range(1, 6):
        print(f"Index {i}th: {log.get_last(i)}")
