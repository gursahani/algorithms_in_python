class Solution:
    def pivotIndex(self, nums):
        sum_left = 0
        total_sum = sum(nums)
        for i in range(len(nums)):
            right_sum = total_sum - sum_left - nums[i]
            if sum_left == right_sum:
                return i
            sum_left += nums[i]
        return -1

if __name__ == '__main__':
    s = Solution()
    print(s.pivotIndex([1,7,3,6,5,6]))
