# Problem: Subarray Product Less Than K - https://leetcode.com/problems/subarray-product-less-than-k/

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = 0
        ans = 0
        current_product = 1

        for right, value in enumerate(nums):
            current_product *= value

            while left <= right and current_product >= k:
                current_product //= nums[left]
                left += 1
            
            ans += right - left + 1
        return ans