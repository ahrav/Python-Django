import sys

def matrix_product(matrix):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return 0
    min_cache = [[[] for x in range(len(matrix))] for j in range(len(matrix[0]))]
    max_cache = [[[] for x in range(len(matrix))] for j in range(len(matrix[0]))]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == 0 and j == 0:
                min_cache[i][j] = matrix[i][j]
                max_cache[i][j] = matrix[i][j]
                continue
            max_val = -sys.maxsize-1
            min_val = sys.maxsize
            if i > 0:
                temp_max = max(matrix[i][j] * max_cache[i-1][j], matrix[i][j] * min_cache[i-1][j])
                max_val = max(max_val, temp_max)
                temp_min = min(matrix[i][j] * max_cache[i-1][j], matrix[i][j] * min_cache[i-1][j])
                min_val = min(min_val, temp_min)
            if j > 0:
                temp_max = max(matrix[i][j] * max_cache[i][j-1], matrix[i][j] * min_cache[i][j-1])
                max_val = max(max_val, temp_max)
                temp_min = min(matrix[i][j] * max_cache[i][j-1], matrix[i][j] * min_cache[i][j-1])
                min_val = min(min_val, temp_min)
            min_cache[i][j] = min_val
            max_cache[i][j] = max_val
    return max_cache[len(matrix)-1][len(matrix[0])-1]
            

print (matrix_product([[-1,2,3],[4,5,-6],[7,8,9]]))
