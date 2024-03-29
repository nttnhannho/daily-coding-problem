"""
[Easy]

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


def main():
    solution = Solution()
    print(solution.isAnagram("anagram", "nagaram"))
    print(solution.isAnagram("rat", "car"))


if __name__ == "__main__":
    main()
