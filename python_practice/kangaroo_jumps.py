def kangaroo(x1, v1, x2, v2):
    if x2 > x1 and v2 > v1 or x1 > x2 and v1 > v2:
        return "NO"
    elif x1 < x2 and v1 == v2 or x2 < x1 and v2 == v1:
        return "NO"
    else:
        if x1 > x2:
            head = x1
            head_jump = v1
            tail = x2
            tail_jump = v2
        else:
            head = x2
            head_jump = v2
            tail = x1
            tail_jump = v1

        crossed = False
        while not crossed:
            if x1 == x2:
                return "YES"
            if tail > head:
                crossed = True
            else:
                if head == x1:
                    return kangaroo(head + head_jump, head_jump, tail + tail_jump, tail_jump)
                else:
                    return kangaroo(tail + tail_jump, tail_jump, head + head_jump, head_jump)
        return "NO"

print (kangaroo(0,3,4,2))