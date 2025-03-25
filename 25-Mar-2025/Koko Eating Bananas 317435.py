# Problem: Koko Eating Bananas - https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEat(mid):
            hours = 0
            for p in piles:
                hours += math.ceil(p/mid)
            return hours <= h

        left, right = 1, max(piles)
        best = right
        mid = 0
        while left <= right:
            mid = left + (right - left)//2
            if canEat(mid):
                best = mid
                right = mid - 1
            else:
                left = mid + 1
        return best
