def rotate_word(string, num):
    for i in range(num):
        last = string[-1]
        new_string = string[:-1]
        string = last + new_string
    return string

print (rotate_word('abcd', 2))


INT_BITS = 32
def left_rotate(number, shift):
    return (number << shift) | (number >> (INT_BITS - shift))

def right_rotate(number, shift):
    return (number >> shift) | (number << (INT_BITS - shift)) & 0xFFFFFFFF
print (right_rotate(16,2))
