# Problem: Minimum Time to Repair Cars - https://leetcode.com/problems/minimum-time-to-repair-cars/

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def helper(time):
            total = 0
            for r in ranks:
                total += int(sqrt((time//r)))
            return total >= cars

        left = 1
        right = min(ranks) * cars * cars
        best = right

        while left <= right:
            mid = left + (right - left) // 2
            if helper(mid):
                right = mid - 1
                best = mid
            else:
                left = mid + 1
        return best