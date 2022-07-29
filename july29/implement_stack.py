# Question: Design a Data Structure SpecialStack that supports all the stack operations like push(), pop(), isEmpty(), isFull() and an
# additional operation getMin() which should return minimum element from the SpecialStack. All these operations of SpecialStack must be O(1).
# To implement SpecialStack, you should only use standard Stack data structure and no other data structure like arrays, list etc.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top=None
        self.count=0
        self.max=None

    def getMax(self):
        if self.max is None:
            print("Empty stack")
        else:
            print(self.max)

    def getCount(self):
        print(self.count)

    def push(self, value):
        if self.top is None:
            self.top = Node(value)
            self.max = value
        else:
            self.top.next = Node(value)

        self.count += 1
        # Set maximum
        if value > self.max:
            self.max = value



stack = Stack()

stack.push(3)
stack.push(5)
stack.getMax()
