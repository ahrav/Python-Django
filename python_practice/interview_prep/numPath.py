def numPaths(n):
  count = [[1 for x in range(n)] for y in range(n)]

  for x in range(n):
    for y in range(n):
      if y > x:
        count[x][y] = 0
  
  for i in range(1, n):
    for j in range(1, i+1):
      count[i][j] = count[i-1][j] + count[i][j-1]
  print(count)
  return count[n-1][n-1]


print(numPaths(4))

