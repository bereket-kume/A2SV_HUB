# Problem: Rotate Array - https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        def reverse_sub_array(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        k=k%n
        reverse_sub_array(0, n-1)
        reverse_sub_array(0, k-1)
        reverse_sub_array(k, n-1)
            
        