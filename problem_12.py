"""
[Hard]

This problem was asked by Amazon.

There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N,
write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2
"""


def solution(n_steps):
    prev = 1
    prev_2 = 1

    for _ in range(2, n_steps + 1):
        curr = prev + prev_2
        prev_2 = prev
        prev = curr
    return prev


def main():
    n_steps = 4
    print(solution(n_steps))


if __name__ == "__main__":
    main()
