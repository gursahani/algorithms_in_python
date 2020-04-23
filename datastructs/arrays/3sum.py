class Solution:
    def threeSum(self, nums):
        nums.sort()
        vis = set()
        result = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                sm = nums[i] + nums[l] + nums[r]
                if sm == 0:
                    combo = [nums[i], nums[l], nums[r]]
                    t = tuple(combo)
                    if t not in vis:
                        vis.add(t)
                        result.append(combo)
                    l += 1
                    r -= 1
                elif sm > 0:
                    r -= 1
                else:
                    l += 1

        return result


if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([-2, 0, 1, 1, 2]))
