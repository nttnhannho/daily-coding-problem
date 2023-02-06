"""
[Easy]

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefixes = []
        min_str_len = min([len(s) for s in strs])
        for i in range(min_str_len):
            char = set(s[i] for s in strs)
            if len(char) != 1:
                break
            prefixes.extend(char)

        return ''.join(prefixes)


def main():
    solution = Solution()
    print(solution.longestCommonPrefix(["flower", "flow", "flight"]))
    print(solution.longestCommonPrefix(["dog", "racecar", "car"]))


if __name__ == "__main__":
    main()
