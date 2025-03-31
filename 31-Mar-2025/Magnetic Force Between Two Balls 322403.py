# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def valid(distance):
            count = 1
            end = position[0]
            for i in range(1, len(position)):
                if position[i] - end >= distance:
                    count += 1
                    end = position[i]
                    if count == m:
                        return True
            return False

        l, r = 1, position[-1] - position[0]
        best = 0

        while l <= r:
            mid = l + (r -l)//2
            if valid(mid):
                best = mid
                l = mid + 1
            else:
                r = mid - 1
        return best