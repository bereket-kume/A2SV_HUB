# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0:1}

        current_sum = 0
        count = 0

        for i in range(len(nums)):

            current_sum += nums[i]

            if current_sum - k in prefix:
                count += prefix[current_sum - k]
            
            if current_sum not in prefix:
                prefix[current_sum] = 1
            else:
                prefix[current_sum] += 1
        return count
