def selectionSort(A, n):
    for i in range(n):
        min_val = A[i]
        min_idx = i
        for j in range(i + 1, n):
            if A[j] < min_val:
                min_val = A[j]
                min_idx = j
        # Swapping
        A[i], A[min_idx] = A[min_idx], A[i]


A = [5, 3,8, 1,2]
selectionSort(A, len(A))
print("Sorted array is:", A) 
