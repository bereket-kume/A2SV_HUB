# Problem: Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        count=1
        points.sort(key=lambda x: x[1])
        min_end = points[0][1]
        
        for i in range(1, len(points)):
            if min_end >= points[i][0]:
                continue
            else:
                count  += 1
                min_end = points[i][1]

        return count

            
        