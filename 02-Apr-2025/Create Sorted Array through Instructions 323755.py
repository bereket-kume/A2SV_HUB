# Problem: Create Sorted Array through Instructions - https://leetcode.com/problems/create-sorted-array-through-instructions/

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        cost = 0
        mod = 10**9 + 7
        sorted_list = SortedList()

        for i in instructions:
            less_count = sorted_list.bisect_left(i)
            greater_count = len(sorted_list) - sorted_list.bisect_right(i)
            cost += min(less_count, greater_count)
            cost %= mod

            sorted_list.add(i)
        return cost
