# Problem: Longest Subarray of 1's After Deleting One Element - https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zeros = 0
        start = 0
        window = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1
            while zeros > 1:
                if nums[start] == 0:
                    zeros -= 1
                start += 1
            window = max(window, i - start)
        return window