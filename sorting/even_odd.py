"""
You are given an integer array arr of size n.
Group and rearrange them (in-place) into evens
and odds in such a way that group of all even
integers appears on the left side and group of all
odd integers appears on the right side.
Example
Input: [1, 2, 3, 4]
Output: [4, 2, 1, 3]
Order does not matter. Other valid solutions
are:
[2, 4, 1, 3]
[2, 4, 3, 1]
[4, 2, 3, 1]
"""


class Solution:
    def even_odd(self, arr):
        lo = 0
        hi = len(arr) - 1
        while lo < hi:
            if arr[lo] % 2 == 0:
                lo += 1
            else:
                arr[hi], arr[lo] = arr[lo], arr[hi]
                hi -= 1
        return arr

if __name__ == '__main__':
    s = Solution()
    print(s.even_odd([1, 2, 3, 4, 5, 8, 7, 9, 10, 12, 11]))
