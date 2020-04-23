class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums3 = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                nums3.append(nums1[i])
                i += 1
            else:
                nums3.append(nums2[j])
                j += 1
        while i < len(nums1):
            nums3.append(nums1[i])
            i += 1
        while j < len(nums2):
            nums3.append(nums2[j])
            j += 1
        print(nums3)
        mid = len(nums3) // 2
        if len(nums3) % 2 == 1:
            return nums3[mid]
        else:
            return (nums3[mid] + nums3[mid - 1]) / 2
# 0, 1, 2, 3, 4, 5, 6
# 1, 2, 3, 4, 5, 7, 9



if __name__ == '__main__':
    s = Solution()
    print(s.findMedianSortedArrays([1, 2], [3, 4]))
