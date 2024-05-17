def insertion_sort(A, n):
    for i in range(1, n):
        value = A[i]
        j = i
        while j > 0 and A[j-1] > value:
            A[j] = A[j-1]
            j = j - 1
        A[j] = value

A = [5, 8, 3, 1, 2]
insertion_sort(A, len(A))
print(A)
