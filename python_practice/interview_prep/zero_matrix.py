def zero_matrix(matrix):
    if not len(matrix) or not len(matrix[0]):
        return
    row_zero = False
    col_zero = False
    for b in matrix[0]:
        if b:
            row_zero = True
    for arr in matrix:
        if arr[0]:
            col_zero = True
    for i in range(1,len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[i][j]:
                matrix[i][0] = True
                matrix[0][j] = True
    for i in range(1,len(matrix)):
        if matrix[0][i]:
            for j in range(1, len(matrix[i])):
                matrix[i][j] = True
    for j in range(len(matrix[0])):
        if matrix[0][j]:
            for i in range(1, len(matrix[j])):
                matrix[i][j] = True
    if row_zero:
        for i in range(len(matrix[0])):
            matrix[0][i] = True
    if col_zero:
        for i in range(len(matrix)):
            matrix[i][0] = True
