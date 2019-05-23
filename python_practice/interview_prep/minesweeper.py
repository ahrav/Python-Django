def mine_sweeper(bombs, num_rows, num_cols):

    cache = [[0 for x range(len(num_cols))] for y in range(len(num_rows))]

    for location in bombs:
        (row, col) = location
        cache[row][col] = -1

    for location in bombs:
        (row, col) = location
        

    # for i in range(len(num_cols)):
    #     for j in range(len(num_rows)):
    #         if i == 0 and j == 0 and cache[i][j] == -1:
    #             if cache[i+1][j] >= 0:
    #                 cache[i+1][j] += 1
    #             if cache[i+1][j+1] >= 0:
    #                 cache[i+1][j+1] += 1
    #             if cache[i][j+1] >= 0:
    #                 cache[i][j+1] += 1