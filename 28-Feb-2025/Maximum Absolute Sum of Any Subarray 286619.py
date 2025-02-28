# Problem: Maximum Absolute Sum of Any Subarray - https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
       
        n = len(nums)

        min_p=max_p=0
        maxa=0
        prefix = 0

        for i in range(n):
            prefix += nums[i]
            maxa = max(maxa, abs(prefix - min_p), abs(prefix - max_p))

            min_p = min(min_p, prefix)
            max_p = max(max_p, prefix)
            
        return maxa

    

