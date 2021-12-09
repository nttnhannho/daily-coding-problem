"""
[Hard]

This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space.
In other words, find the lowest positive integer that does not exist in the array.
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""


def solution01(nums):
    length = len(nums)

    if not nums or 1 not in nums:
        return 1

    for index, num in enumerate(nums):
        if num <= 0 or num > length:
            #  Transform all negative numbers, 0 and number > length into 1
            num = 1
            nums[index] = num

        index = num - 1
        if nums[index] > 0:
            nums[index] = -1 * nums[index]

    for index, num in enumerate(nums):
        if num > 0:
            return index + 1

    return length + 1


def solution02(nums):
    s = set(nums)
    i = 1
    while i in s:
        i += 1
    return i


if __name__ == "__main__":
    sample1 = [3, 4, -1, 1]
    sample2 = [1, 2, 0]
    sample3 = [7, 4, -3, 8, 1, 2]
    sample4 = [1, 2, 3, 4, 5, 6]
    sample5 = [1, 2, 3, 4, 5, 7]
    sample6 = [1, 2, 3, 4, 5, 8]
    sample7 = [4, 2, 6]

    print(solution01(sample1))
    print(solution01(sample2))
    print(solution01(sample3))
    print(solution01(sample4))
    print(solution01(sample5))
    print(solution01(sample6))
    print(solution01(sample7))

    print("--------------------")
    sample1 = [3, 4, -1, 1]
    sample2 = [1, 2, 0]
    sample3 = [7, 4, -3, 8, 1, 2]
    sample4 = [1, 2, 3, 4, 5, 6]
    sample5 = [1, 2, 3, 4, 5, 7]
    sample6 = [1, 2, 3, 4, 5, 8]
    sample7 = [4, 2, 6]

    print(solution02(sample1))
    print(solution02(sample2))
    print(solution02(sample3))
    print(solution02(sample4))
    print(solution02(sample5))
    print(solution02(sample6))
    print(solution02(sample7))
