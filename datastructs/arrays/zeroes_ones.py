class Solution:
    def zeroes_ones(self, arr):
        lo = 0
        hi = len(arr) - 1
        while lo < hi:
            if arr[lo] == 0:
                lo += 1
            else:
                arr[lo], arr[hi] = arr[hi], arr[lo]
                hi -= 1
        return arr


if __name__ == '__main__':
    s = Solution()
    print(s.zeroes_ones([0, 1, 0, 1, 1, 1]))