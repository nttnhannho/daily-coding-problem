"""
[Hard]

This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of
all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was
[3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""
from functools import reduce


def get_product(input_):
    """
    Return the product of all elements in the input list.
    :param input_: input list
    :return: integer product
    """
    return reduce(lambda x, y: x * y, input_)


def solution(nums):
    result = []
    if len(nums) < 2:
        return []
    for index, num in enumerate(nums):
        if index == 0:
            new_num = get_product(nums[1:])  # Get product of all elements except the 1st one.
        elif index == len(nums) - 1:
            new_num = get_product(nums[:-1])  # Get product of all elements except the last one.
        else:  # Get product of all elements except the middle one.
            # Split the input list into 2 parts: left and right.
            # Get product of both left and right, then plus them together.
            left = nums[:index]
            right = nums[index + 1:]
            new_left_num = get_product(left)
            new_right_num = get_product(right)
            new_num = new_left_num * new_right_num
        result.append(new_num)
    return result


if __name__ == "__main__":
    sample1 = [1, 2, 3, 4, 5]
    sample2 = [3, 2, 1]
    sample3 = [1]
    sample4 = []

    print(solution(sample1))
    print(solution(sample2))
    print(solution(sample3))
    print(solution(sample4))
