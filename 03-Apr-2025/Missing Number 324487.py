# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()

        left, right = 0, len(nums)

        while left < right:
            mid = left + (right - left)//2
            if nums[mid] > mid:
                right = mid
            else:
                left = mid + 1

        return left