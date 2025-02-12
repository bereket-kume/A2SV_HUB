# Problem: Partition Labels - https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = defaultdict(int)
        print(len(s))

        for i in range(len(s)):
            last_index[s[i]] = i

        
        result = []
        size = 0
        end = 0

        for idx, val in enumerate(s):
            size += 1
            if last_index[val] > end:
                end = last_index[val]

            if end == idx:
                result.append(size)
                size = 0

        return result
