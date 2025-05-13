# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        arr_xor = 0
        range_xor = 0

        for i in range(len(nums) + 1):
            range_xor ^= i
        
        for num in nums:
            arr_xor ^= num
        
        return range_xor ^ arr_xor