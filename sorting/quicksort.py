import random


def quick_sort(arr, lo, hi):
    if lo < hi:
        q = partition(arr, lo, hi)
        quick_sort(arr, lo, q - 1)
        quick_sort(arr, q + 1, hi)


def partition(arr, lo, hi):
    i = lo - 1
    for j in range(lo, hi):
        if arr[j] < arr[hi]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[hi] = arr[hi], arr[i+1]
    return i + 1


def swap(a, b):
    temp = a
    a = b
    b = temp


arr = [3, 5, 7, 1, 9, 10, 12]
n = len(arr)
quick_sort(arr, 0, n - 1)

print(arr)