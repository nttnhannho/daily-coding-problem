"""
[Easy]

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""


def is_found(lst, k):
    seen = {}  # Empty dict to store seen numbers
    for num in lst:
        diff = k - num  # Get difference of k and current number in sample list
        if diff in seen:
            return True
        seen[num] = True  # Add number to dict
    return False


if __name__ == "__main__":
    sample_lst = [10, 15, 3, 7]
    for k in range(30):
        if is_found(sample_lst, k):
            print(k)
