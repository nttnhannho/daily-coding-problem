"""
[Hard]

This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers.
Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10,
since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
"""


def solution(lst):
    if len(lst) <= 2:
        return max(0, max(lst))

    max_excluding_last = max(0, lst[0])
    max_including_last = max(max_excluding_last, lst[1])

    for num in lst[2:]:
        prev_max_including_last = max_including_last
        max_including_last = max(max_including_last, max_excluding_last + num)
        max_excluding_last = prev_max_including_last

    return max(max_including_last, max_excluding_last)


if __name__ == "__main__":
    print(solution([2, 4, 6, 2, 5]))
    print(solution([5, 1, 1, 5]))
    print(solution([1, 5, 1, 5]))
