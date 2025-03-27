# Problem: Zero Array Transformation II - https://leetcode.com/problems/zero-array-transformation-ii/

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        l,r = 0, len(queries)

        def possible(arr, mid):
            diff = [0] * (len(arr))
            for i in range(mid):
                left, right, val = queries[i]
                diff[left] += val
                if right + 1 < len(arr):
                    diff[right + 1] -= val

            for i in range(1, len(arr)):
                diff[i] += diff[i-1]

            for i in range(len(arr)):
                if arr[i] > diff[i]:
                    return False
            return True

        best = -1
        while l <= r:
            mid = (l+r)//2
            if possible(nums, mid):
                best = mid
                r = mid-1
            else:
                l = mid+1
        return best