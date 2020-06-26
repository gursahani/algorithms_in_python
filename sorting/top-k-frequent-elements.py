#https://leetcode.com/problems/top-k-frequent-elements/
import heapq
import collections


class Solution:
    def topKFrequent(self, nums, k: int):
        c = collections.Counter(nums)
        print(c)

        heap = []
        out = []
        for item, freq in c.items():
            heapq.heappush(heap, (-freq, item))

        for _ in range(k):
            freq, item = heapq.heappop(heap)
            out.append(item)

        return out
