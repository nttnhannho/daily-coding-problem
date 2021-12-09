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


def count_tree(root):
    count = [0]
    count_subtree(root, count)
    return count[0]


def count_subtree(root, count):
    if not root:
        return True
    left = count_subtree(root.left, count)
    right = count_subtree(root.right, count)
    if not left or not right:
        return False
    if root.left and root.val != root.left.val:
        return False
    if root.right and root.val != root.right.val:
        return False
    count[0] += 1
    return True


if __name__ == "__main__":
    root = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
    print(count_tree(root))
