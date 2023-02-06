"""
[Easy]

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""


def solution(nums, k):
    seen = set()  # Empty set to store seen numbers
    for num in nums:
        if k - num in seen:
            return True
        seen.add(num)  # Add number to set
    return False


def main():
    sample_lst = [10, 15, 3, 7]
    for k in range(30):
        if solution(sample_lst, k):
            print(k)


if __name__ == "__main__":
    main()
