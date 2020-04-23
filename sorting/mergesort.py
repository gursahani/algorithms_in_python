def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    arr1 = merge_sort(arr[:mid])
    arr2 = merge_sort(arr[mid:])

    return merge(arr1, arr2)


def merge(arr1, arr2):
    arr3 = []
    i = j = 0

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


print(merge_sort([3, 5, 7, 1, 9, 10, 12]))
