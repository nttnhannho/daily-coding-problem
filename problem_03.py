"""
[Medium]

This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s),
which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root):
    if root is None:
        return "#"
    return f"{root.val} {serialize(root.left)} {serialize(root.right)}"


def deserialize(data):
    vals = iter(data.split())

    def helper():
        val = next(vals)
        if val == "#":
            return None
        node_ = Node(val)
        node_.left = helper()
        node_.right = helper()
        return node_
    return helper()


def main():
    node = Node("root", Node("left", Node("left.left")), Node("right"))

    try:
        print(serialize(node))
        print(deserialize(serialize(node)).val == "root")

        print(serialize(node.left))
        print(deserialize(serialize(node)).left.val == "left")

        print(serialize(node.left.left))
        print(deserialize(serialize(node)).left.left.val == "left.left")

        print(serialize(node.right))
        print(deserialize(serialize(node)).right.val == "right")

        print(serialize(node.right.right))
        print(deserialize(serialize(node)).right.right.val == "#")
    except AttributeError:
        print("Node is not existed")


if __name__ == "__main__":
    main()
