"""
[Easy]

This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:
   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solution(root):
    count, _ = count_subtrees(root)
    return count


def count_subtrees(root):
    if not root:
        return 0, True

    left_count, is_left_unival = count_subtrees(root.left)
    right_count, is_right_unival = count_subtrees(root.right)
    total = left_count + right_count

    if is_left_unival and is_right_unival:
        if root.left and root.val != root.left.val:
            return total, False
        if root.right and root.val != root.right.val:
            return total, False
        return total + 1, True

    return total, False


def main():
    root = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
    print(solution(root))


if __name__ == "__main__":
    main()
