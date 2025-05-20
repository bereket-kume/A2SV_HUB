# Problem: Bitwise XOR of All Pairings - https://leetcode.com/problems/bitwise-xor-of-all-pairings/description/?envType=problem-list-v2&envId=brainteaser

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        xor1=0
        for num in nums1:
            xor1 ^= num
        xor2 = 0
        for num in nums2:
            xor2 ^= num

        result = 0
        if n % 2:
            result ^= xor1
        if m % 2:
            result ^= xor2
        return result