"""
[Easy]

Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

Constraints:
1 <= s.length <= 105
s[i] is a printable ascii character.
"""
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        # s.reverse()
        s_len = len(s)
        for i in range(s_len // 2):
            if s[i] != s[s_len - 1 - i]:
                s[i], s[s_len - 1 - i] = s[s_len - 1 - i], s[i]


if __name__ == "__main__":
    solution = Solution()

    sample1 = ["h", "e", "l", "l", "o"]
    solution.reverseString(sample1)
    print(sample1)

    sample2 = ["H", "a", "n", "n", "a", "h"]
    solution.reverseString(sample2)
    print(sample2)
