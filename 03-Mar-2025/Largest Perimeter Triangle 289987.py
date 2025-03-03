# Problem: Largest Perimeter Triangle - https://leetcode.com/problems/largest-perimeter-triangle/

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        max_per = 0

        for i in range(2, len(nums)):
    
            if nums[i-2] + nums[i-1] > nums[i]:
                max_per = max(max_per, (nums[i-2]+ nums[i-1]+nums[i]))
                 
        return max_per
