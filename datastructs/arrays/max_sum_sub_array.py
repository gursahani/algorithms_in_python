import math


def max_sum_sub_array(arr):
    current_sum = total_sum = arr[0]

    for i in range(1, len(arr)):
        current_sum = max(current_sum + arr[i], arr[i])

        total_sum = max(total_sum, current_sum)

    return total_sum


arr1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_sum_sub_array(arr1))


def binary_search(arr, num):
    lo = 0
    hi = len(arr) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        if num < arr[mid]:
            hi = mid - 1

        elif num > arr[mid]:
            lo = mid + 1
        elif num == arr[mid]:
            return mid

    return -1


arr2 = [1, 9, 11, 14, 15, 20, 25, 50]
print(binary_search(arr2, 51))


def max_sum_sub_arr(arr, lo, hi):
    if lo == hi - 1:
        return lo, hi, arr[lo]
    else:

        mid = (lo + hi) // 2
        left_lo, left_hi, left_sum = max_sum_sub_arr(arr, lo, mid)
        right_lo, right_hi, right_sum = max_sum_sub_arr(arr, mid + 1, hi)
        cross_lo, cross_hi, cross_sum = max_cross_sub_arr(arr, lo, mid, hi)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_lo, left_hi, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_lo, right_hi, right_sum
        else:
            return cross_lo, cross_hi, cross_sum


def max_cross_sub_arr(arr, lo, mid, hi):
    left_sum = -2000
    sum = 0
    for i in range(mid, lo, -1):
        sum += arr[i]
        if left_sum < sum:
            left_sum = sum
            max_left = i

    right_sum = -2000
    sum = 0
    for j in range(mid + 1, hi + 1):
        sum += arr[j]
        if right_sum < sum:
            right_sum = sum
            max_right = j

    return max_left, max_right, left_sum + right_sum


def find_max_subarray(alist, start, end):
    """Returns (l, r, m) such that alist[l:r] is the maximum subarray in
    A[start:end] with sum m. Here A[start:end] means all A[x] for start <= x <
    end."""
    # base case
    if start == end - 1:
        return start, end, alist[start]
    else:
        mid = (start + end) // 2
        left_start, left_end, left_max = find_max_subarray(alist, start, mid)
        right_start, right_end, right_max = find_max_subarray(alist, mid, end)
        cross_start, cross_end, cross_max = find_max_crossing_subarray(alist, start, mid, end)
        if (left_max > right_max and left_max > cross_max):
            return left_start, left_end, left_max
        elif (right_max > left_max and right_max > cross_max):
            return right_start, right_end, right_max
        else:
            return cross_start, cross_end, cross_max


def find_max_crossing_subarray(alist, start, mid, end):
    """Returns (l, r, m) such that alist[l:r] is the maximum subarray within
    alist with start <= l < mid <= r < end with sum m. The arguments start, mid,
    end must satisfy start <= mid <= end."""
    sum_left = float('-inf')
    sum_temp = 0
    cross_start = mid
    for i in range(mid - 1, start - 1, -1):
        sum_temp = sum_temp + alist[i]
        if sum_temp > sum_left:
            sum_left = sum_temp
            cross_start = i

    sum_right = float('-inf')
    sum_temp = 0
    cross_end = mid + 1
    for i in range(mid, end):
        sum_temp = sum_temp + alist[i]
        if sum_temp > sum_right:
            sum_right = sum_temp
            cross_end = i + 1
    return cross_start, cross_end, sum_left + sum_right


alist = [-8, -2, -3, -4, -5, -9]
start, end, maximum = find_max_subarray(alist, 0, len(alist))
print('The maximum subarray starts at index {}, ends at index {}'
      ' and has sum {}.'.format(start, end - 1, maximum))
