def negative_numbers(arr):
    if not len(arr) or not len(arr[0]):
        return []
    count = 0
    col = len(arr[0])-1
    row = 0
    while row < len(arr) and col >=0:
        if arr[row][col] < 0:
            count += col +1
            row += 1
        else:
            col -= 1
        
    return count

print(negative_numbers([[-3, -2, -1, 1], [-2, 2, 3, 4], [4, 5, 7, 8]]))
