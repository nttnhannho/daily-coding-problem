"""
[Easy]

Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore, it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore, it is not a palindrome.
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if self.reverse(x) != x:
            return False
        return True

    @staticmethod
    def reverse(x: int) -> int:
        upper_bound = 2 ** 31 - 1
        lower_bound = -2 ** 31
        if x >= 0:
            return int(str(x)[::-1]) if lower_bound <= int(str(x)[::-1]) <= upper_bound else 0
        return int(f'-{(str(x)[1:])[::-1]}') if lower_bound <= int(f'-{(str(x)[1:])[::-1]}') <= upper_bound else 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.isPalindrome(121))
    print(solution.isPalindrome(-121))
    print(solution.isPalindrome(10))
