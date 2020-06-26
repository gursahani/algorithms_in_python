#973 k-closest-points-to-origin

#https://leetcode.com/problems/k-closest-points-to-origin/

import heapq
from typing import List
from math import sqrt


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        dist = 0
        heap = []
        for point in points:
            print(point)
            dist = sqrt(point[0] ** 2 + point[1] ** 2)
            heapq.heappush(heap, (dist, point))

        out = []
        for _ in range(K):
            out.append(heapq.heappop(heap)[1])

        return out