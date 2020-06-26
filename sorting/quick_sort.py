"""
Quicksort algo:

1. Choose pivot(can be first element or random element)
2. Arrange all elements less than pivot on the left of the pivot
3. Arrange all elements greater than pivot on the right of the pivot
4. Repeat steps 1-3 recursively on both sides of the pivot element

"""


def quick_sort(arr, lo, hi):

    if lo < hi:
        pivot = partition(arr, lo, hi)
        quick_sort(arr, lo, pivot - 1)
        quick_sort(arr, pivot+1, hi)

def partition(arr, lo, hi):
    pivot = arr[hi]
    index = lo - 1
    for j in range(lo, hi):
        if arr[j] <= pivot:
            index += 1
            arr[j], arr[index] = arr[index], arr[j]
    arr[index+1], arr[hi] = arr[hi], arr[index+1]
    return index + 1



arr = [3, 5, 8, 4, 7, 11, 2]
n = len(arr)
quick_sort(arr, 0, n-1)
print(arr)

