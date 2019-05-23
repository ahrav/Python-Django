class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def lca(root, n1, n2):
    if n1 == n2:
        return n1
    path_to_n1 = path_to_node(root, n1)
    path_to_n2 = path_to_node(root, n2)
    if not path_to_n1 or not path_to_n2:
        return None
    prev = None
    while path_to_n1 and path_to_n2:
        s = path_to_n1.pop(0)
        t = path_to_n2.pop(0)
        if s == t:
            prev = s
        else:
            break
        return prev

def path_to_node(root, n):
    if root is None:
        return None
    if root == n:
        stack = []
        stack.append(root)
        return stack
    left = path_to_node(root.left, n)
    if left:
        left.append(root)
        return left

    right = path_to_node(root.right, n)
    if right:
        right.append(root)
        return right
    return None

n = Node(1)
m = Node(3)
k = Node(2)
l = Node(4)
n.left = m
n.right = k
m.left = l

print(lca(n, l, k))
