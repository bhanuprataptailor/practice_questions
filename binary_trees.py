class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root=None):
        if root:
            node = Node(root)
            self.root = node
        else:
            self.root = None

    def insert(self, val):
        node = Node(val)
        if not self.root:
            self.root = node
            return
        cur_node = self.root
        checked_nodes = [cur_node]

        while True:
            if not checked_nodes[0].left:
                checked_nodes[0].left = node
                print(f"Inserted -> {val} at {checked_nodes[0].val} left child")
                return
            else:
                checked_nodes.append(checked_nodes[0].left)

            if not checked_nodes[0].right:
                checked_nodes[0].right = node
                print(f"Inserted -> {val} at {checked_nodes[0].val} right child")
                return
            else:
                checked_nodes.append(checked_nodes[0].right)

            checked_nodes = checked_nodes[1:]

    def print(self):
        cur_node = self.root
        checked_nodes = [cur_node]
        while len(checked_nodes) != 0:
            print(checked_nodes[0].val, flush=True, end=' ')
            if checked_nodes[0].left:
                checked_nodes.append(checked_nodes[0].left)
            if checked_nodes[0].right:
                checked_nodes.append(checked_nodes[0].right)
            checked_nodes = checked_nodes[1:]

    def inorder(self, root=None):
        if not root:
            root = self.root

        if root.left:
            self.inorder(root.left)
        print(root.val, end=" ")

        if root.right:
            self.inorder(root.right)

    def preorder(self, root=None):
        if not root:
            root = self.root

        print(root.val, end=" ")

        if root.left:
            self.preorder(root.left)

        if root.right:
            self.preorder(root.right)

    def postorder(self, root=None):
        if not root:
            root = self.root

        if root.left:
            self.postorder(root.left)

        if root.right:
            self.postorder(root.right)

        print(root.val, end=" ")


"""
I am inserting the below tree : [a, b, c, d, e, 'NULL', f]
         a 
       /  \
      b    c
    /   \   \
   d     e   f
"""

elements = ['a', 'b', 'c', 'd', 'e', 'NULL', 'f']

print("\n\n----INSERTION TO TREE----")
bt = BinaryTree()
for element in elements:
    bt.insert(element)

print("\n\n----TREE----")
bt.print()

print("\n\n----INORDER----")
bt.inorder()

print("\n\n----PREORDER----")
bt.preorder()

print("\n\n----POSTORDER----")
bt.postorder()
