"""
[Easy]

This problem was asked by Amazon.

Implement a stack that has the following methods:

push(val), which pushes an element onto the stack
pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack, then it should throw an error or return null.
max(), which returns the maximum value in the stack currently. If there are no elements in the stack, then it should throw an error or return null.
Each method should run in constant time.
"""
from abc import ABC, abstractmethod


class StackADT(ABC):
    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def push(self, val):
        pass

    @abstractmethod
    def pop(self):
        pass

    @abstractmethod
    def max(self):
        pass


class Stack(StackADT):
    def __init__(self):
        self.stack = []

    def __str__(self):
        return f"{[item for item in self.stack]}"

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if not self.stack:
            return None

        return self.stack.pop()

    def max(self):
        if not self.stack:
            return None

        return max(self.stack)


class StackCreator:
    def __init__(self, stack):
        self.stack = stack

    def __str__(self):
        return str(self.stack)

    def push(self, val):
        self.stack.push(val)

    def pop(self):
        return self.stack.pop()

    def max(self):
        return self.stack.max()



def main():
    stack_obj = Stack()
    stack = StackCreator(stack_obj)
    stack.push(1)
    stack.push(43)
    stack.push(15)
    stack.push(10)
    print(f"Item: {stack}")
    popped_item = stack.pop()
    print(f"Popped item: {popped_item}")
    print(f"Largest item: {stack.max()}")

if __name__ == "__main__":
    main()