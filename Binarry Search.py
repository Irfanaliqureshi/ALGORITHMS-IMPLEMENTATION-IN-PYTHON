def binarySearch(a, beg, end, item):
    if beg > end:
        return -1
    else:
        mid = (beg + end) // 2
        if item == a[mid]:
            return mid
        elif item < a[mid]:
            return binarySearch(a, beg, mid - 1, item)
        else:
            return binarySearch(a, mid + 1, end, item)

def result(index):
    if index != -1:
        print("Item found at index:", index)
    else:
        print('Item not found')

a = [1, 2, 3, 4, 5, 7, 8, 9, 10]
item = 5
index = binarySearch(a, 0, len(a) - 1, item)
result(index)
