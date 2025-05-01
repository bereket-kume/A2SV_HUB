# Problem: Maximum Sum With at Most K Elements - https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/description/

class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        total = []
        for row, limit in zip(grid, limits):
            temp = row[:]
            heapq.heapify(temp)

            while len(temp) > limit:
                heapq.heappop(temp)
            total.extend(temp)
            
        heapq.heapify(total)
        while len(total) > k:
            heapq.heappop(total)
        return sum(total)