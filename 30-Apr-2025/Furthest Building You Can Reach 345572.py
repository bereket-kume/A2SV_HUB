# Problem: Furthest Building You Can Reach - https://leetcode.com/problems/furthest-building-you-can-reach/

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        min_heap = []

        for i in range(n-1):
            climb = heights[i+1] - heights[i]

            if climb <= 0:
                continue

            heappush(min_heap, climb)
            
            if len(min_heap) > ladders:
                smallest_climb = heapq.heappop(min_heap)
                bricks -= smallest_climb

                if bricks < 0:
                    return i

        return n - 1