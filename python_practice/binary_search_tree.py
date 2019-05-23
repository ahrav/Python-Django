class Node:
    
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            current_node = self.root
            while True:
                if value < current_node.value:
                    if current_node.left is None:
                        current_node.left = new_node
                        return
                    current_node = current_node.left
                else:
                    if current_node.right is None:
                        current_node.right = new_node
                        return
                    current_node = current_node.right

    def search(self, value):
        if self.root is None:
            return "Tree is empty"
        current_node = self.root
        while current_node:
            if value < current_node.value:
                current_node = current_node.left
            elif value > current_node.value:
                current_node = current_node.right
            elif value == current_node.value:
                return current_node
        return "Couldn't find it"


tree = BinarySearchTree()
tree.insert(10)
tree.insert(15)
tree.insert(20)
tree.insert(5)
tree.insert(12)
print(tree.search(12))
print(tree.root.left.value)