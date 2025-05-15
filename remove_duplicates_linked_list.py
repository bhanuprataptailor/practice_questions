# Problem Statement
"""
Write code to remove duplicates from and unsorted linked list
Ex: Input:-> [1->2->4->2->6]
    Output: -> [1->2->4->6]

Complexities:
Time: Insertion to list takes O(N), Duplicate Removal -> O(N)
Space: Generated list will be dependent on number of elements O(N),
    Duplicate Removal -> O(N) extra space because of dictionary to store the traversed elements

"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_the_end(self, values):
        for val in values:
            node = Node(val)
            if not self.tail:
                self.tail = node
                self.head = node
            else:
                self.tail.next = node
                self.tail = node

    def show_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.val, end='->')
            cur_node = cur_node.next

    def remove_duplicates(self):
        elements_traversed = {}
        cur_node = self.head
        prev_node = cur_node
        while cur_node:
            if cur_node.val not in elements_traversed:
                elements_traversed[cur_node.val] = True
            else:
                prev_node.next = cur_node.next
            prev_node = cur_node
            cur_node = cur_node.next


list1 = LinkedList()
elements = [6, 2, 4, 2, 1, 1, 6, 3]
list1.insert_at_the_end(elements)
print(list1.head.val, list1.tail.val)
print("The original List")
list1.show_list()
list1.remove_duplicates()
print("\nList after duplicates removal")
list1.show_list()
