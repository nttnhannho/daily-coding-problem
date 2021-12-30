"""
[Medium]

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the
signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21
"""


class Solution:
    def reverse(self, x: int) -> int:
        upper_bound = 2**31 - 1
        lower_bound = -2**31
        if x >= 0:
            return int(str(x)[::-1]) if lower_bound <= int(str(x)[::-1]) <= upper_bound else 0
        return int(f'-{(str(x)[1:])[::-1]}') if lower_bound <= int(f'-{(str(x)[1:])[::-1]}') <= upper_bound else 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.reverse(123))
    print(solution.reverse(-123))
    print(solution.reverse(120))
