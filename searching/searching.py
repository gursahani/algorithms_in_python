class Searching:

    def __init__(self, arr, target):
        self.arr = arr
        self.target = target

    def __str__(self):
        return f'Arr: {self.arr}, target: {self.target}'

    def binary_search(self):
        left = 0
        right = len(self.arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.target > self.arr[mid]:
                left = mid + 1

            elif self.target < self.arr[mid]:
                right = mid - 1

            elif self.target == self.arr[mid]:
                return mid

        return -(left + 1)

    def insertInPlace(self, arr, target):
        idx = self.binary_search()
        if idx < 0:
            arr.insert(-(idx + 1), target)
            return arr
        arr.insert(idx, target)

        # for i in range(len(arr)):
        #     if target < arr[i]:
        #         arr.insert(i, target)
        #         return arr
        # arr.append(target)
        return arr

    def binary_search_rec(self):
        return self.binary_search_helper(self.arr, 0, len(self.arr) - 1, self.target)

    def binary_search_helper(self, arr, left, right, target):
        if left <= right:
            mid = (left + right) // 2
            if target == arr[mid]:
                return mid
            elif target > arr[mid]:
                return self.binary_search_helper(arr, mid + 1, right, target)
            elif target < arr[mid]:
                return self.binary_search_helper(arr, left, mid - 1, target)

        else:
            return -1

    def foo(self):
        times_table = [i for i in range(1, 11)]
        for num in times_table:
            print(num)


if __name__ == '__main__':
    s = Searching([1, 4, 5, 8, 9, 10, 12], 7)
    # print(str(s))
    #
    # print(s.binary_search())
    # print(s.insertInPlace([1, 4, 5, 8, 9, 10, 12], 7))
    # print(s.binary_search_rec())
    s.foo()
