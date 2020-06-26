def duplicateZeros(arr):
    """
    Do not return anything, modify arr in-place instead.
    """

    for i in range(len(arr)):
        if arr[i] == 0:
            arr[i+1:] = arr[i:-1]
            i += 2
        # i += 1
    return arr


print(duplicateZeros([1,0,2,3,0,4,5,0]))