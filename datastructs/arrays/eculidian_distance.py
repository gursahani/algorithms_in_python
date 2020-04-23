class Solution:
    # [1, 3, 5, 8, 9, 11]
    def euclidian_distance(self, nums):
        mySet = set()
        for i in range(1, len(nums)):
            for j in range(i-1, i):
                mySet.add(nums[i] - nums[j])
        print(mySet)
        return min(list(mySet))

    def euclidian_dist_sublinear(self, nums):
        sorted_nums = sorted(nums)
        min_dist = 1000
        # print(sorted_nums)
        for i in range(1, len(sorted_nums)):
            dist = sorted_nums[i] - sorted_nums[i-1]
            # print("dist is ", dist)
            if min_dist > dist:
                min_dist = dist
                # print(dist, min_dist)

        return min_dist

    def euclidian_dist_div_conq(self, nums):
        lo = 0
        hi = len(nums) - 1
        min_dist = 1000
        mid = (lo + hi) // 2
        while lo <= hi:
            dist = nums[mid] - nums[lo]
            if min_dist > abs(dist):
                min_dist = abs(dist)
                lo += 1
            if lo == mid:
                dist = nums[mid] - nums[hi]
                if min_dist > abs(dist):
                    min_dist = abs(dist)
                hi -= 1
        return min_dist


if __name__ == '__main__':
    s = Solution()
    twodnums = [[1, 0], [3, 0], [5, 0], [8, 0], [9, 0], [11, 0]]
    print(s.euclidian_distance([1, 3, 5, 8, 9, 11]))
    print(s.euclidian_dist_sublinear([1, 3, 5, 8, 9, 11]))
    print(s.euclidian_dist_div_conq([1, 3, 5, 8, 9, 11]))
