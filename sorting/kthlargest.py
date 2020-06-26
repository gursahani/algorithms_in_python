import heapq


class KthLargest:

    def __init__(self, k: int, nums):
        self.k = k
        self.nums = nums
        self.h = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heapq.heappush(self.h, val)

        if len(self.h) > self.k:
            heapq.heappop(self.h)

        return self.h[0]

# Your KthLargest object will be instantiated and called as such:
nums = [5, 6, 4, 9, 3]
obj = KthLargest(2, nums)
param_1 = obj.add(3)
print(param_1)
# 4, 5, 8, 2 => add(3) => 4, 5, 8, 2, 3 => return 4
# 4, 5, 8, 2, 3 => add(5) => 4, 5,8, 2, 3, 5 => return