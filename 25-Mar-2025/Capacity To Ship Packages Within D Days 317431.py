# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(mid):
            ships, currentWeight = 1, mid
            for w in weights:
                if currentWeight - w < 0:
                    ships += 1
                    currentWeight = mid
                currentWeight -= w
            return ships <= days

        left, right = max(weights), sum(weights)
        best=right
        
        while left <= right:
            mid = left + (right - left)// 2
            if canShip(mid):
                best = min(best, mid)
                right = mid - 1
            else:
                left = mid + 1
        return best