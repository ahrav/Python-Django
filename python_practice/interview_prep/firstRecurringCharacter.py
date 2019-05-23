def first_recurring_char(arr):
    if not arr:
        return None
    char_count = set()
    for x in arr:
        if x in char_count:
            return x
        else:
            char_count.add(x)
    return None

print(first_recurring_char([2, 5, 1, 2, 3, 5, 1, 2, 4]))
print(first_recurring_char([]))