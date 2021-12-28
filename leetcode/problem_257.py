"""
[Easy]

Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.

Example 1:
Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]

Example 2:
Input: root = [1]
Output: ["1"]

Constraints:
The number of nodes in the tree is in the range [1, 100].
-100 <= Node.val <= 100
"""
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []

        def get_tree_path(node, path, res):
            if not node:
                return res

            if not node.left and not node.right:
                res.append(path)
                return res

            if node.left:
                get_tree_path(node.left, path + f"->{node.left.val}", res)
            if node.right:
                get_tree_path(node.right, path + f"->{node.right.val}", res)

            return res

        return get_tree_path(root, f"{root.val}", [])


if __name__ == "__main__":
    pass
