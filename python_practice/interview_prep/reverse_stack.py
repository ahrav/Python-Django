def insert_at_bottom(arr, x):
    if not arr:
        arr.append(x)
        return
    temp = arr.pop(0)
    insert_at_bottom(arr, x)
    arr.append(temp)

def reverse_stack(arr):
    if not arr:
        return arr
    temp = arr.pop(0)
    reverse_stack(arr)
    insert_at_bottom(arr, temp)
    return arr