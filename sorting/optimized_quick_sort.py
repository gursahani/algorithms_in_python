def quicksort(arr, left, right):

    if left < right:
        pivot = partition(arr, left, right)
        quicksort(arr, left, pivot - 1)
        quicksort(arr, pivot + 1, right)



def partition(arr, left, right):
    i = left + 1
    p = arr[left]
    for j in range(left+1, right+1):
        if arr[j] < p:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1

    arr[i-1], arr[left] = arr[left], arr[i-1]

    return i - 1





arr = [12, 1, 23, 4, 5, 9, 11, 2]
quicksort(arr, 0, len(arr) - 1)
print(arr)