def merge(arr1, arr2):
    i = j = 0
    arr3 = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] > arr2[j]:
            arr3.append(arr2[j])
            j += 1
        else:
            arr3.append(arr1[i])
            i += 1

    while i < len(arr1):
        arr3.append(arr1[i])
        i += 1

    while j < len(arr2):
        arr3.append(arr2[j])
        j += 1

    return arr3


def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr

    mid = n // 2

    arr1 = merge_sort(arr[:mid])
    arr2 = merge_sort(arr[mid:])

    return merge(arr1, arr2)


print(merge_sort([3, 4, 1, 6, 2, 5, 8, 7]))
