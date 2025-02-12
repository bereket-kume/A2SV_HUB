# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        maximum_water=0

        while left < right:
            min_height = min(height[left], height[right])
            width = right - left
            area = width * min_height

            if height[left] > height[right]:
                right -= 1
            elif height[right] > height[left]:
                left += 1
            else:
                left += 1
                right -= 1

            maximum_water = max(maximum_water, area)

        return maximum_water