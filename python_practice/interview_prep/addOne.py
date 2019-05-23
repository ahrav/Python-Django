def add_one(arr):
    result = [0] * len(arr)
    carry = 1
    for i in range(len(arr)-1, -1,-1):
        sum = carry + arr[i]
        if sum == 10:
            carry = 1
        else:
            carry = 0
        result[i] = sum % 10
    if carry:
        result = [0] * (len(arr)+1)
        result[0] = 1
    return result

print(add_one([1, 2, 3]))
print(add_one([1, 2, 9]))
print(add_one([9, 9, 9]))