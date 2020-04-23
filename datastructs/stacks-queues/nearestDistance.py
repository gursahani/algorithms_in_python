import sys


class FindNearestDistance:
    def __init__(self):
        self.map = {}

    def find_distance(self, arr):
        for i in range(len(arr)):
            if arr[i] in self.map:
                self.map.update(arr[i], i - self.map.get(arr[i]))
            else:
                self.map.update(arr[i], i)
        min_distance = sys.maxsize

        for x in self.map.values():
            if min_distance > x:
                min_distance = x

        return min_distance


if __name__ == '__main__':

    f = FindNearestDistance
    arr = [1, 2, 3, 4, 10, 3, 2, 4, 7]
    f.find_distance(arr)
