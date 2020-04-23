class Solution:
    def even_odd(self, nums):
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            if nums[lo] % 2 == 0:
                lo += 1
            else:
                nums[lo], nums[hi] = nums[hi], nums[lo]
                hi -= 1
        return nums


if __name__ == '__main__':
    s = Solution()
    print(s.even_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
