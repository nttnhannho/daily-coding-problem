"""
[Hard]

This problem was asked by Google.

An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields,
it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list;
it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and
dereference_pointer functions that converts between nodes and memory addresses.
"""
import ctypes


class Node:
    def __init__(self, val):
        self.val = val
        self.both = 0


class XORLinkedList:
    @staticmethod
    def __get_obj(id_):
        return ctypes.cast(id_, ctypes.py_object).value

    def __init__(self):
        self.head = None
        self.tail = None
        self.__nodes = []

    def __str__(self):
        return f"{[item.val for item in self.__nodes]}"

    def add(self, node):
        new_node = Node(node)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.both = id(new_node) ^ self.tail.both
            new_node.both = id(self.tail)
            self.tail = new_node
        self.__nodes.append(new_node)

    def get(self, index):
        prev_id = 0
        node = self.head
        for i in range(index):
            next_id = prev_id ^ node.both

            if next_id:
                prev_id = id(node)
                node = XORLinkedList.__get_obj(next_id)
            else:
                raise IndexError("Out of range")

        return node.val


if __name__ == "__main__":
    xor_ll = XORLinkedList()
    xor_ll.add(1)
    xor_ll.add(23)
    xor_ll.add(6)
    print(xor_ll)
    print(xor_ll.get(0))
    print(xor_ll.get(1))
    print(xor_ll.get(2))
