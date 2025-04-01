# Problem: Split Array Largest Sum - https://leetcode.com/problems/split-array-largest-sum/

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        def is_possible(mid):
            current_sum = 0
            split = 1

            for num in nums:
                current_sum += num

                if current_sum  > mid:
                    split += 1
                    current_sum = num
                    if split > k:
                        return False
            return True

        l, r = max(nums), sum(nums)
        best = 0

        while l <= r:
            mid = l + (r - l)//2

            if is_possible(mid):
                best = mid
                r = mid - 1
            else:
                l = mid + 1

        return best
