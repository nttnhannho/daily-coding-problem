"""
[Medium]

This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair.
For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
Implement car and cdr.
"""


def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def car(func):
    return func(lambda a, b: a)


def cdr(func):
    return func(lambda a, b: b)


def main():
    a1, b1 = 1, 2
    a2, b2 = 3, 4
    a3, b3 = 10, 0

    print(cons(a1, b1))
    print(cons(a2, b2))
    print(cons(a3, b3))

    print(car(cons(a1, b1)))  # Result = 1
    print(car(cons(a2, b2)))  # Result = 3
    print(car(cons(a3, b3)))  # Result = 10

    print(cdr(cons(a1, b1)))  # Result = 2
    print(cdr(cons(a2, b2)))  # Result = 4
    print(cdr(cons(a3, b3)))  # Result = 0


if __name__ == "__main__":
    main()
