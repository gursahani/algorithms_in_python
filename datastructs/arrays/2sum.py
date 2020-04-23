class Solution:
    def twoSum(self, nums, target):
        m = dict()
        l = []
        for i in range(len(nums)):
            if target - nums[i] in m.keys():
                l.append(m[target - nums[i]])
                l.append(i)
            m[nums[i]] = i
        return l


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([3, 2, 4, 5], 8))
