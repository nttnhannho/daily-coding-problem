"""
[Easy]

Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is
returned.

Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        res = 0
        if x == 0 or x == 1:
            return x
        start = 1
        end = x
        while start <= end:
            mid = (start + end) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                start = mid + 1
                res = mid
            else:
                end = mid - 1
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.mySqrt(4))
    print(solution.mySqrt(8))
    print(solution.mySqrt(16))
    print(solution.mySqrt(11))
