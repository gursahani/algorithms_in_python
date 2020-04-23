import random


class Sorting:

    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr)//2
        b = self.merge_sort(arr[:mid])
        c = self.merge_sort(arr[mid:])
        return self.merge(b, c)

    def merge(self, b, c):
        a = []
        i = j = 0
        while i < len(b) and j < len(c):
            if b[i] <= c[j]:
                a.append(b[i])
                i += 1
            else:
                a.append(c[j])
                j += 1

        while i < len(b):
            a.append(b[i])
            i += 1

        while j < len(c):
            a.append(c[j])
            j += 1

        return a

    def insertion_sort(self, arr):
        for i in range(1, len(arr)):
            self.insert(arr, i, arr[i])
        return arr

    def insert(self, arr, idx, value):
        i = idx - 1
        while i >= 0 and arr[i] > value:
            arr[i + 1] = arr[i]
            i = i - 1

        arr[i + 1] = value

    def in_sort(self, arr):
        for i in range(1, len(arr)):
            current = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > current:
                arr[j + 1] = arr[j]
                j = j - 1
            arr[j + 1] = current
        return arr


if __name__ == '__main__':
    x = [4, 9, 8, 1, 10, 2, 11, 6]
    print(x)
    s = Sorting()
    print(s.insertion_sort(x))
    print(s.in_sort(x))
    print(s.merge_sort(x))
