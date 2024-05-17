def knapsack(wt, val, n, m):
    v = [[0 for _ in range(m+1)] for _ in range(n+1)]
    
    for i in range(0, n+1):
        for w in range(0, m+1):
            if i == 0 or w == 0:
                v[i][w] = 0
            elif wt[i-1] <= w:
                v[i][w] = max(v[i-1][w], val[i-1] + v[i-1][w-wt[i-1]])
            else:
                v[i][w] = v[i-1][w]
    
    return v[n][m]

def knapsack_backtrack(wt, val, n, m):
    v = [[0 for _ in range(m+1)] for _ in range(n+1)]
    
    for i in range(1, n+1):
        for w in range(1, m+1):
            if wt[i-1] <= w:
                v[i][w] = max(val[i-1] + v[i-1][w-wt[i-1]], v[i-1][w])
            else:
                v[i][w] = v[i-1][w]

    i, w = n, m
    while i > 0 and w > 0:
        if v[i][w] != v[i-1][w]:
            print("Item", i, "with weight", wt[i-1], "and value", val[i-1])
            w -= wt[i-1]
            i -= 1
        else:
            i -= 1


wt = [3, 2, 4, 1]
val = [300, 200, 400, 100]
n = len(val)
m = 5
print("Maximum value:", knapsack(wt, val, n, m))
knapsack_backtrack(wt, val, n, m)
