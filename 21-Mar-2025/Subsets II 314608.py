# Problem: Subsets II - https://leetcode.com/problems/subsets-ii/

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        def helper(start, sub):
            ans.append(sub[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue

                sub.append(nums[i])
                helper(i + 1, sub)
                sub.pop()
                
        helper(0, [])
        return ans