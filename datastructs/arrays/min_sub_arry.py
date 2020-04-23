#LC-209
# Created by Kunal Gursahani at 10-25-2019 5:45 PM
# Last updated at 10-25-2019 5:45 PM

# Input: s = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: the subarray [4,3] has the minimal length under the problem constraint.

from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:

        left = 0
        right = len(nums) - 1
        while left <= right:
            pass
        return s


