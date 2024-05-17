def max_heapify(A, heapsize, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i

    if left <= heapsize and A[left] > A[i]:
        largest = left
    if right <= heapsize and A[right] > A[largest]:
        largest = right

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, heapsize, largest)

def build_max_heap(A):
    heapsize = len(A) - 1
    for i in range(len(A) // 2 - 1, -1, -1):
        max_heapify(A, heapsize, i)


A = [5, 8, 3, 2, 1]
build_max_heap(A)
print(A)  
