# Problem: Longest Nice Subarray - https://leetcode.com/problems/longest-nice-subarray/

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        max_len = 0
        current_or = 0
        l = 0

        for r in range(len(nums)):

            while current_or & nums[r] != 0:
                current_or ^= nums[l]
                l += 1
            current_or |= nums[r]
            max_len = max(max_len, r-l+1)

        return max_len