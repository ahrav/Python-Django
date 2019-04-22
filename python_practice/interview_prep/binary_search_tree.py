class Node:
    def __init__(self, val):
        self.value = val
        self.right = None
        self.left = None
    
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

tree_vals = []

def inorder(tree):
    if tree is not None:
        inorder(tree.getLeftChild())
        tree_vals.append(tree.getRootVal())
        inorder(tree.getRighChild())

def check_bst(tree_vals):
    return tree_vals == sorted(tree_vals)

