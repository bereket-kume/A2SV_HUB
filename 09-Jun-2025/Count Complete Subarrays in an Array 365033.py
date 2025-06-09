# Problem: Count Complete Subarrays in an Array - https://leetcode.com/problems/count-complete-subarrays-in-an-array/

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        element = len(set(nums))
        ans = 0
        r = 0
        count = {}

        for i in range(n):
            if i > 0:
                remove = nums[i - 1]
                count[remove] -= 1
                if count[remove] == 0:
                    count.pop(remove)
            while r < n and len(count) < element:
                add = nums[r]
                count[add] = count.get(add, 0) + 1
                r += 1
            if len(count) == element:
                ans += n - r + 1
        return ans