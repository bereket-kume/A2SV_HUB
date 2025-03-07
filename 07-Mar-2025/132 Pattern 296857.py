# Problem: 132 Pattern - https://leetcode.com/problems/132-pattern/

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        stack = []
        min_val = float('inf')

        for i in range(n):
            while stack and stack[-1][1] <= nums[i]:
                stack.pop()

            if stack and stack[-1][0] < nums[i]:
                return True
            min_val = min(min_val, nums[i])
            stack.append((min_val, nums[i]))

        return False
