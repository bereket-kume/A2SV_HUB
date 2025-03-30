# Problem: Heaters - https://leetcode.com/problems/heaters/

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        def check(radius):
            house, heater = len(houses), len(heaters)
            l, r = 0, 0

            while l < house:
                if r >= heater:
                    return False
                max_range = heaters[r] + radius
                min_range = heaters[r] - radius

                if houses[l] < min_range:
                    return False
                
                if houses[l] > max_range:
                    r += 1
                else:
                    l += 1
            return True

        l = 0
        r = max(max(houses), max(heaters)) - min(min(houses), min(heaters))
        best = 0

        while l < r:
            mid = l + (r - l)//2
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return l