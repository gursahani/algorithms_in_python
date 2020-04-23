def move_zeroes(nums):
    count = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            count += 1
            nums[count] = nums[i]

    while count < len(nums):
        nums[count] = 0

    return nums


print(move_zeroes([1, 0, 5, 0, 1]))
