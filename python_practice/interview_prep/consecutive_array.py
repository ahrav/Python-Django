def consecutive(arr):
    values = set()
    for i in arr:
        values.add(i)
    curr_max = 0
    for i in values:
        if i-1 in values:
            continue
        length = 0
        while i in values:
            i += 1
            length += 1
            curr_max = max(curr_max, length)
    return curr_max



def consectuive_array(arr):
    vals = set()
    for i in arr:
        set.add(i)
    max_val = 0
    for x in vals:
        if x-1 in vals:
            continue
        length = 0
        while x in vals:
            x += 1
            length += 1
            max_val = max(length, max_val)
    return max_val
