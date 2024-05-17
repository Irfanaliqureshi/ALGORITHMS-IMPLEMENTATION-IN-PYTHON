def bubbleSort(A, n):
    for k in range(n-1):
        for i in range(n-k-1):
            if A[i] > A[i+1]:
                # Swap elements
                A[i], A[i+1] = A[i+1], A[i]


A = [3,7, 3, 8, 1, 2]
bubbleSort(A, len(A))
print(A)  
