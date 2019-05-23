def find_intersection(list1, list2):
    if list1 is None or list2 is None:
        return None
    res1 = get_tail_size(list1)
    res2 = get_tail_size(list2)

    if res1.tail != res2.tail:
        return None

    if res1.size < res2.size:
        shorter = list1
        longer = list2
    else:
        shorter = list2
        longer = list1

    
    shorter = list1 if res1.size < res2.size else list2
    longer = list2 if res1.size < res2.size else list1

    longer = get_kth_node(longer, abs(res1.size - res2.size))

    while shorter != longer:
        shorter = shorter.next
        longer = longer.next
    return longer


class Result:
    def __init__(self, tail, size):
        self.tail = tail
        self.size = size

def get_tail_size(head):
    if head is None:
        return None
    curr = head
    size = 1
    while curr.next is not None:
        size += 1
        curr = curr.next
    return Result(curr, size)

def get_kth_node(head, k):
    curr = head
    while k > 0 and curr is not None:
        curr = curr.next
        k -= 1
    return curr