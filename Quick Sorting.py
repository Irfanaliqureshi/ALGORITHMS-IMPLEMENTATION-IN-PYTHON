def quickSort(A, start, end):
    if start >= end:
        return
    
    q = partition(A, start, end)
    quickSort(A, start, q-1)
    quickSort(A, q+1, end)

def partition(A, start, end):
    pivot = A[end]
    index = start
    for i in range(start, end):
        if A[i] <= pivot:
            A[i], A[index] = A[index], A[i]
            index += 1
    A[index], A[end] = A[end], A[index]
    return index


A = [10, 7, 8, 9, 1, 5]
quickSort(A, 0, len(A)-1)
print("Sorted array is:", A) 
