# Problem: Permutations - https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def helper(start):
            if start == len(nums):
                ans.append(nums[:])
                return
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                helper(start + 1)
                nums[start], nums[i] = nums[i], nums[start]

        helper(0)
        return ans