### sorted 2D array
def matrix_search(arr, x):
    if not arr or not arr[0]:
        return False
    row = 0
    col = len(arr) - 1

    while row < len(arr[0]) and col >= 0:
        if arr[row][col] == x:
            return True
        if arr[row][col] < x:
            row += 1
        else:
            col -= 1
    return False
                
