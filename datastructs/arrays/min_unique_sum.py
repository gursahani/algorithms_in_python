"""
first sort the array, and store its sum
then create new array by incrementing each duplicate element with maximum value of itself+1 and previous element. do this in place
store the sum of newly created array
the difference between the two sums is the total number of incrementes made
before arr = [1, 1, 1, 1, 3, 5], sum1 = 12
after arr = [1, 2, 3, 4, 5, 6] sum2 = 21
total moves = 21 - 12 = 9
"""


class Solution:
    def minIncrementForUnique(self, arr):
        arr.sort()
        s1 = sum(arr)
        n = len(arr)
        for i in range(1, n): 
            if arr[i] <= arr[i - 1]:
                arr[i] = max(arr[i], arr[i-1]+1)
        s2 = sum(arr)
        return s2 - s1



if __name__ == '__main__':
    s = Solution()
    print(s.minIncrementForUnique([1, 1, 1, 1, 3, 5]))