# Problem: Count Subarrays Where Max Element Appears at Least K Times - https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_val = max(nums)
        ans=start=window=0

        for end in range(len(nums)):
            if nums[end] == max_val:
                window += 1
            while window == k:
                if nums[start] == max_val:
                    window -= 1
                start += 1
            ans += start    
        return ans