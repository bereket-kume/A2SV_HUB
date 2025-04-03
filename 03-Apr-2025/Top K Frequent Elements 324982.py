# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        sorted_count = list(count.keys())
        sorted_count.sort(key=count.get, reverse=True)
        return sorted_count[:k]
