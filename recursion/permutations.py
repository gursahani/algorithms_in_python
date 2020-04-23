class Solution:
    def permute(self, nums):
        output = []
        return self.permuteHelper(nums, output)

    def permuteHelper(self, nums, output):
        if not nums:
            return output
        else:
