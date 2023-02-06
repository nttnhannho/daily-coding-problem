"""
[Easy]

Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Example 2:
Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_split = s.split()
        if len(pattern) != len(s_split):
            return False

        d_ = {}
        s_ = set()

        for index, p_item in enumerate(pattern):
            s_item = s_split[index]

            if p_item in d_:
                if d_[p_item] != s_item:
                    return False
            else:
                if s_item in s_:
                    return False

            d_[p_item] = s_item
            s_.add(s_item)

        return True


def main():
    solution = Solution()
    print(solution.wordPattern("abba", "dog cat cat dog"))
    print(solution.wordPattern("abba", "dog cat cat fish"))
    print(solution.wordPattern("aaaa", "dog cat cat dog"))


if __name__ == "__main__":
    main()
