"""
[Hard]

This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space.
In other words, find the lowest positive integer that does not exist in the array.
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""


def find_smallest_positive_number(numbers):
    length = len(numbers)

    if not numbers or 1 not in numbers:
        return 1

    for index, num in enumerate(numbers):
        if num <= 0 or num > length:
            #  Transform all negative numbers, 0 and number > length into 1
            num = 1
            numbers[index] = num

        index = num - 1
        if numbers[index] > 0:
            numbers[index] = -1 * numbers[index]

    for index, num in enumerate(numbers):
        if num > 0:
            return index + 1

    return length + 1


if __name__ == "__main__":
    sample1 = [3, 4, -1, 1]
    sample2 = [1, 2, 0]
    sample3 = [7, 4, -3, 8, 1, 2]
    sample4 = [1, 2, 3, 4, 5, 6]
    sample5 = [1, 2, 3, 4, 5, 7]
    sample6 = [1, 2, 3, 4, 5, 8]
    sample7 = [4, 2, 6]

    print(find_smallest_positive_number(sample1))
    print(find_smallest_positive_number(sample2))
    print(find_smallest_positive_number(sample3))
    print(find_smallest_positive_number(sample4))
    print(find_smallest_positive_number(sample5))
    print(find_smallest_positive_number(sample6))
    print(find_smallest_positive_number(sample7))
