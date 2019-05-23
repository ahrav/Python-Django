class Node:
    def __init__(self, data):
        self.value = data
        self.right = None
        self.left = None

def binary_insert(root, node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.left is None:
                root.left = node
            else:
                binary_insert(root.left, node)
        else:
            if root.right is None:
                root.right = node
            else:
                binary_insert(root.right, node)

def breadth_first_search(root):
    list_values = []
    queue = [root]
    while queue:
        current_node = queue.pop(0)
        list_values.append(current_node)
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)
    return list_values

def depth_first_search_inorder(root):
    return traverse_inorder(root, [])

def traverse_inorder(root, lst):
    if root is not None:
        traverse_inorder(root.left, lst)
        lst.append(root.data)
        traverse_inorder(root.right, lst)
    return lst

def depth_first_search_preorder(root):
    return traverse_inorder(root, [])

def traverse_preorder(root, lst):
    if root is not None:
        lst.append(root.data)
        traverse_inorder(root.left, lst)
        traverse_inorder(root.right, lst)
    return lst

def depth_first_search_postorder(root):
    return traverse_inorder(root, [])

def traverse_postorder(root, lst):
    if root is not None:
        traverse_inorder(root.left, lst)
        traverse_inorder(root.right, lst)
        lst.append(root.data)
    return lst

def breadth_first_search_recursive(root, lst):
    if not queue:
        return lst
    queue = [root]
    current_node = queue.pop(0)
    lst.append(current_node)
    if current_node.left:
            queue.append(current_node.left)
    if current_node.right:
        queue.append(current_node.right)
    return breadth_first_search_recursive(queue, lst)

def verify_bst(root):
    return sorted(depth_first_search_inorder(root)) == depth_first_search_inorder(root)

def get_height(root):
    return -1 if root is None else 1 + max(get_height(root.left), get_height(root.right))

def tree_max(node):
    if not node:
        return float("-inf")
    max_left = tree_max(node.left)
    max_right = tree_max(node.right)
    return max(max_left, max_right, node.value)

def tree_min(node):
    if not node:
        return float("inf")
    min_left = tree_min(node.left)
    min_right = tree_min(node.right)
    return min(min_left, min_right, node.value)

def is_bst(node):
    if not node:
        return True
    if tree_max(node.left) < node.value < tree_min(node.right) and is_bst(node.left) and is_bst(node.right):
        return True
    else:
        return False


# class Node:
#     def __init__(self,data):
#         self.right=self.left=None
#         self.data = data


# class BST:
#     def insert(self,root,data):
#         if root==None:
#             return Node(data)
#         else:
#             if data<=root.data:
#                 cur=self.insert(root.left,data)
#                 root.left=cur
#             else:
#                 cur=self.insert(root.right,data)
#                 root.right=cur
#         return root

#     def getHeight(self, root):
#         return -1 if root is None else 1 + max(self.getHeight(root.left), self.getHeight(root.right))

#     def tree_max(self, root):
#         if not root:
#             return float("-inf")
#         max_left = self.tree_max(root.left)
#         max_right = self.tree_max(root.right)
#         return max(max_left, max_right, root.value)

#     def tree_min(self, root):
#         if not root:
#             return float("inf")
#         min_left = self.tree_min(root.left)
#         min_right = self.tree_min(root.right)
#         return min(min_left, min_right, root.value)

#     def is_bst(self, root):
#         if not root:
#             return True
#         if self.tree_max(root.left) < root.value < self.tree_min(root.right) and self.is_bst(root.left) and self.is_bst(root.right):
#             return True
#         else:
#             return False

# tree_vals = []
# def inorder(root):
#     if root is not None:
#         inorder(root.left)
#         tree_vals.append(root.data)
#         inorder(root.right)


class BinaryTree(object):
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t


    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    def breadth_first_search(self):
        list_values = []
        queue = [self.key]
        while queue:
            current_node = queue.pop(0)
            list_values.append(current_node)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        return list_values

# tree_vals = []

# def inorder(tree):
#     if tree is not None:
#         inorder(tree.getLeftChild())
#         tree_vals.append(tree.getRootVal())
#         inorder(tree.getRighChild())

# def check_bst(tree_vals):
#     return tree_vals == sorted(tree_vals)

