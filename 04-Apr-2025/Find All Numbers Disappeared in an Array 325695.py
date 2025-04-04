# Problem: Find All Numbers Disappeared in an Array - https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        i = 0
        while i < n:
            pos = nums[i] - 1
            if nums[i] != nums[pos]:
                nums[i], nums[pos] = nums[pos], nums[i]
            else:
                i += 1

        for i in range(n):
            if nums[i] - 1 != i:
                ans.append(i+1)
        return ans