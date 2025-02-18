# Problem: Maximum subarray - https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        
        if n == 0:
            return 0

        prefix = [0] * n
        prefix[0] = nums[0]
        min_prefix = 0
        maxsum=nums[0]

        for i in range(1, n):
            prefix[i] = nums[i] + prefix[i-1]
        
        for i in range(n):
            maxsum = max(maxsum, prefix[i]-min_prefix)
            min_prefix = min(min_prefix, prefix[i])
        return maxsum