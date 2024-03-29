"""
[Easy]

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
"""


class Solution:
    def isValid(self, s: str) -> bool:
        bracket_dict = {
            "(": ")",
            "[": "]",
            "{": "}",
            ")": None,
            "]": None,
            "}": None
        }
        stack = []
        for bracket in s:
            if len(stack) and bracket == stack[-1]:
                stack.pop()
            else:
                stack.append(bracket_dict[bracket])

        return len(stack) == 0


def main():
    solution = Solution()
    print(solution.isValid("()"))
    print(solution.isValid("()[]{}"))
    print(solution.isValid("(]"))


if __name__ == "__main__":
    main()
