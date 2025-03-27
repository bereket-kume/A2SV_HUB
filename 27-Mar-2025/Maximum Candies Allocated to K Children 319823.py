# Problem: Maximum Candies Allocated to K Children - https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def possible(mid):
            total = 0
            for candy in candies:
                total += candy // mid
            return total >= k
        
        l, r = 1, max(candies)
        best = 0

        while l <= r:
            mid = (r + l)// 2
            if possible(mid):
                best = mid
                l = mid + 1
            else:
                r = mid - 1 
        return best