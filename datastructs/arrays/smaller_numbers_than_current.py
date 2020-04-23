class Solution:

    def smallerNumbersThanCurrent(self, nums):
        nums2 = sorted(nums)
        cn = {}
        for i in range(len(nums2)):
            if nums2[i] not in cn:
                cn[nums2[i]] = i

        print(cn)
        output = [0]*len(nums)
        for i in range(len(nums)):
            output[i] = cn[nums[i]]
        return output


if __name__ == '__main__':
    s = Solution()
    print(s.smallerNumbersThanCurrent([8, 1, 2, 2, 3]))
