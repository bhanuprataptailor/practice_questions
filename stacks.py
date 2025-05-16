"""
Problem Statement: Design a stack, which have push, pop and min functionality in O(1) time.
push: insert element into stack
pop: remove element from stack
min: find the minimum element from the stack

"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Stack:
    """
    Here the adjustment after the pop, we are adjusting the min value, it's taking O(N) time,
    rest all the operations are O(1) time
    """

    def __init__(self):
        self.top = None
        self.min = None

    def show_stack(self):
        print("----STACK1----")
        cur_node = self.top
        while cur_node:
            print(cur_node.val)
            cur_node = cur_node.next

    def push(self, val):
        print(f"Pushing {val} to Stack1")
        node = Node(val)
        if self.top:
            node.next = self.top
            self.top = node
            # print(self.top.val)
            if node.val < self.min.val:
                self.min = node
        else:
            self.top = node
            self.min = node
            # print(self.top.val)

    def adjust_min(self):
        cur_node = self.top
        while cur_node:
            if cur_node.val < self.min.val:
                self.min = cur_node
            cur_node = cur_node.next

    def pop(self):
        if self.top:
            print(f"Popping the element {self.top.val} from Stack1")
            self.top = self.top.next
            self.min = Node(100000000000000)
            self.adjust_min()
        else:
            print("Stack is Empty, can't pop")

    def get_min(self):
        print(f"Minimum -> {self.min.val}")


class StackOptimized:

    def __init__(self):
        self.top = None
        self.min = None
        self.min_top_map = {}

    def show_stack(self):
        print("----STACK2----")
        cur_node = self.top
        while cur_node:
            print(cur_node.val)
            cur_node = cur_node.next

    def push(self, val):
        print(f"Pushing {val} to Stack2")
        node = Node(val)
        if self.top:
            node.next = self.top
            self.top = node
            # print(self.top.val)
            if node.val < self.min.val:
                self.min = node
        else:
            self.top = node
            self.min = node

        self.min_top_map[self.top] = self.min

    def pop(self):
        if self.top:
            print(f"Popping the element {self.top.val} from Stack2")
            self.top = self.top.next
            self.min = Node(100000000000000)
        else:
            print("Stack is Empty, can't pop")

    def get_min(self):
        print(f"Minimum -> {self.min_top_map[self.top].val}")


elements = [5, 4, 3, 2, 1, 1, 2, 3, 0]
stack1 = Stack()
stack2 = StackOptimized()
for element in elements:
    stack1.push(element)
    stack2.push(element)

stack1.show_stack()
stack1.get_min()
stack2.show_stack()
stack2.get_min()

stack1.pop()
stack2.pop()

stack1.show_stack()
stack1.get_min()
stack2.show_stack()
stack2.get_min()
