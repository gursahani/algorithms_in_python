def naive_quick_sort(arr):
    if len(arr) < 2:
        return arr

    pivot = arr[0]
    left = []
    right = []

    for i in range(1, len(arr)):
        if arr[i] <= pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    left = naive_quick_sort(left)
    right = naive_quick_sort(right)
    left.append(pivot)
    return left + right




print(naive_quick_sort([12, 1, 23, 4, 5, 9, 11, 2]))