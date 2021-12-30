"""
[Easy]

Given a string columnTitle that represents the column title as appear in an Excel sheet,
return its corresponding column number.

For example:
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...

Example 1:
Input: columnTitle = "A"
Output: 1

Example 2:
Input: columnTitle = "AB"
Output: 28

Example 3:
Input: columnTitle = "ZY"
Output: 701
"""


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        for c in columnTitle:
            d = ord(c) - ord("A") + 1
            res = res * 26 + d
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.titleToNumber("A"))
    print(solution.titleToNumber("AB"))
    print(solution.titleToNumber("ZY"))
    print(solution.titleToNumber("AAA"))
