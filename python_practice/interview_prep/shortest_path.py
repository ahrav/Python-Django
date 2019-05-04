class Node:
    def __init__(self):
        self.next = None

def shortest_path(a, b):
    if a is None or b is None:
        return None
    to_visit = []
    parents = {}
    to_visit.append(a)
    parents[a] = None
    while to_visit:
        curr = to_visit.pop(0)
        if curr == b:
            break
        for node in curr:
            if node not in parents:
                to_visit.append(node)
                parents[node] = curr
    if b not in parents:
        return None
    result = []
    curr = b
    while curr is not None:
        result.insert(0,curr)
        curr = parents[curr]
    return result
