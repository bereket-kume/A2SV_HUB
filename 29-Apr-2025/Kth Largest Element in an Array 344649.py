# Problem: Kth Largest Element in an Array - https://leetcode.com/problems/kth-largest-element-in-an-array/description/

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        sorted_val = []

        for _ in range(len(nums)):
            sorted_val.append(heapq.heappop(nums))
        return sorted_val[len(nums) - k]