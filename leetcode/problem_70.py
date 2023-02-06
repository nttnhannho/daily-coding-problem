"""
[Easy]

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        penultimate = 1
        one_before_penultimate = 2

        for i in range(n - 2):
            one_before_penultimate, penultimate = one_before_penultimate + penultimate, penultimate

        return one_before_penultimate


def main():
    solution = Solution()
    print(solution.climbStairs(2))
    print(solution.climbStairs(3))


if __name__ == "__main__":
    main()
