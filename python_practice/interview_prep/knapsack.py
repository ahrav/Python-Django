def knapSack(W, wt, val, n): 
    K = [[0 for x in range(W+1)] for x in range(n+1)] 
  
    # Build table K[][] in bottom up manner 
    for i in range(n+1): 
        for w in range(W+1): 
            if i==0 or w==0: 
                K[i][w] = 0
            elif wt[i-1] <= w: 
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w]) 
            else: 
                K[i][w] = K[i-1][w] 
  
    return K[n][W]


def knappySack(max_weight, weights, values, n):
    cache = [[0 for weight in range(weights+1) for i in range(n+1)]]

    for i in range(n+1):
        for j in range(weights+1):
            if i == 0 or j == 0:
                return 0
            elif weights[i-1] <= j:
                cache[i][j] = max(values(i-1) + cache[i-1][j-weights[i-1]], cache[i-1][j])
            else:
                cache[i][j] = cache[i-1][j]
        return cache[n][max_weight]