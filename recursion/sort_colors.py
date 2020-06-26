"""
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?
"""


class Solution:
    def sort_colors(self, arr):
        self.sort_colors_helper(arr, 0, len(arr) - 1)


    def sort_colors_helper(self, arr, left, right):
        if left < right:
            pivot = self.partition(arr, left, right)
            self.sort_colors_helper(arr, left, pivot - 1)
            self.sort_colors_helper(arr, pivot + 1, right)



    def partition(self, arr, left, right):
        pivot = arr[left]
        i = left + 1
        for j in range(left + 1, right + 1):
            if arr[j] < pivot:
                arr[j], arr[i] = arr[i], arr[j]
                i += 1

        arr[left], arr[i - 1] = arr[i-1], arr[left]
        return i - 1


if __name__ == '__main__':
    s = Solution()
    arr = [2, 0, 1, 0, 2, 1, 1, 0]
    s.sort_colors(arr)
    print(arr)

