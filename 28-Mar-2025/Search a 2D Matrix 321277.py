# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def helper(l, r, nums):
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] == target:
                    return True

                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return False

        left = 0
        right = len(matrix)-1
        while left <= right:
            mid = left + (right - left)//2
            if matrix[mid][0] == target  or matrix[mid][-1] == target:
                return True
            if matrix[mid][0] < target  and matrix[mid][-1] > target:
                return helper(0, len(matrix[0])-1, matrix[mid])
            if target < matrix[mid][-1]:
                right = mid - 1
            else:
                left = mid + 1
        return False
        