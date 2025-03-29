# Problem: H-Index II - https://leetcode.com/problems/h-index-ii/description/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        def valid(mid):
            return citations[mid] >= len(citations) - mid
            
        l, r = 0, len(citations)-1
        best = 0

        while l <= r:
            mid = l + (r - l)//2

            if valid(mid):
                best = len(citations) - mid
                r = mid - 1
            else:
                l = mid + 1
        return best