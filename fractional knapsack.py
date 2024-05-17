def fractional_knapsack(p, w, m, n):
    x = [0] * n  # Initialize x as a list of n zeros
    Rc = m
    
    for i in range(n):
        if w[i] <= Rc:
            x[i] = 1
            Rc -= w[i]
        else:
            x[i] = Rc / w[i]
            Rc = 0
            break  # No need to continue if the sack is full
    
    return x


p = [60, 100, 120]
w = [10, 20, 30]
m = 50
n = len(p)
result = fractional_knapsack(p, w, m, n)
print("Fractions of items taken:", result)
