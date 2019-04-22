def missing_number(arr):
    arr_xor = arr[0]
    total_xor = 1

    for num in range(1,len(arr)):
        arr_xor ^= arr[num]
    for n in range(2, len(arr)+2):
        total_xor ^= n
    return total_xor ^ arr_xor

print (missing_number([1,2,3,4,5,7,8,9]))

def missing_numbers(arr):
    size = len(arr) + 2
    total_sum = size * (size + 1) / 2
    arr_sum = 0

    for num in range(1,len(arr)):
        arr_sum += arr[num]

    pivot = (total_sum - arr_sum) / 2
    total_left_xor = 1
    arr_left_xor = arr[0]
    total_right_xor = arr[(pivot+1)]
    arr_right_xor = arr[pivot]

    for i in range(2, pivot+1):
        total_left_xor ^= i
    for i in range(pivot +2, size + 2):
        total_right_xor ^= i
    for num in arr:
        if num <= pivot:
            arr_left_xor ^= num
        else:
            arr_right_xor ^= num
    return [total_left_xor ^ arr_left_xor, total_right_xor ^ arr_right_xor]

print (missing_numbers([1,2,3,4,5,7,8,9,11]))
