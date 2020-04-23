def jump_to_end(arr):
    max_step = arr[0]
    last_index = len(arr) - 1
    for i in range(len(arr)):
        if max_step >= last_index:
            return True
        else:
            max_step = i + arr[i]
    return False


# a = [3, 2, 0, 0, 1, 2, 1]
# a = [2, 2, 1, 0, 4]
a = [3, 2, 1, 0, 4]
print(jump_to_end(a))
