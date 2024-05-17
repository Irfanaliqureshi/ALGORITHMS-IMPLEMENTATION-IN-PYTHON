def mergeSort(A):
    n = len(A)
    if n < 2:
        return
    else:
        mid = n // 2
        left = A[:mid]
        right = A[mid:]
        
        mergeSort(left)
        mergeSort(right)
        
        merge(left, right, A)

def merge(L, R, A):
    nL = len(L)
    nR = len(R)
    i = j = k = 0
    
    while i < nL and j < nR:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
    
    while i < nL:
        A[k] = L[i]
        i += 1
        k += 1
    
    while j < nR:
        A[k] = R[j]
        j += 1
        k += 1

A = [5,8,3,1, 2]
mergeSort(A)
print( A)
