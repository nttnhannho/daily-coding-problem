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


def generate(numbers):
    result = []
    if len(numbers) == 1:
        return []
    for index, element in enumerate(numbers):
        if index == 0:
            new_element = get_product(numbers[1:])  # Get product of all elements except the 1st one.
        elif index == len(numbers) - 1:
            new_element = get_product(numbers[:-1])  # Get product of all elements except the last one.
        else:  # Get product of all elements except the middle one.
            # Split the input list into 2 parts: left and right.
            # Get product of both left and right, then plus them together.
            left = numbers[:index]
            right = numbers[index + 1:]
            new_left_element = get_product(left)
            new_right_element = get_product(right)
            new_element = new_left_element * new_right_element
        result.append(new_element)
    return result


if __name__ == "__main__":
    sample1 = [1, 2, 3, 4, 5]
    sample2 = [3, 2, 1]

    print(generate(sample1))
    print(generate(sample2))
