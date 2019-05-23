INT_MAX = 4294967296
INT_MIN = -4294967296

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def is_bst(node):
    return is_bst_util(node, INT_MIN, INT_MAX)

def is_bst_util(node, mini, maxi):
    if node is None:
        return True
    if node.data > maxi or node.data <= mini:
        return False
    return (is_bst_util(node.left, mini, node.data) and is_bst_util(node.right, node.data, maxi))


# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

# def is_binary_search_tree(node):
#     return is_binary_search_tree_util(node, INT_MIN, INT_MAX)

# def is_binary_search_tree_util(node, mini, maxi):
#     if node is None:
#         return True
#     if node.value > maxi or node.value < mini:
#         return False
#     return (is_binary_search_tree_util(node.left, mini, node.value) and is_binary_search_tree_util(node.right, node.value, maxi))

