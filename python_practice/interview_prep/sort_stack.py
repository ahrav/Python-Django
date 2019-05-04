def sort_stack(stack):
    if stack is None or len(stack) == 0:
        return stack
    ordered_stack = []
    temp = 0
    ordered_stack.append(stack.pop(0))
    while stack:
        temp = stack.pop(0)
        while ordered_stack and temp > ordered_stack[0]:
            stack.insert(0, ordered_stack.pop(0))
        ordered_stack.insert(0, temp)
    return ordered_stack



the_stck = [4,5,7,3,2]
print (sort_stack(the_stck))
