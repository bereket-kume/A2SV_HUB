# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []

        for i in range(1 << n):
            subset = []

            for j in range(32):
                if i &(1 << j):
                    subset.append(nums[j])
            ans.append(subset)
        return ans