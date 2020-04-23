class AddNumbers:
    def add_numbers(self, arr, total) -> int:
        if len(arr) == 0:
            return total
        else:
            return self.add_numbers(arr, total + arr.pop())


if __name__ == '__main__':
    a = AddNumbers()
    nums = [1, 2, 3, 4, 5]
    print(a.add_numbers(nums, 0))



