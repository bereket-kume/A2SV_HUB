# Problem: Car Pooling - https://leetcode.com/problems/car-pooling/description/

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        m = max(trips, key=lambda x: x[-1])[2]
        
        prefix = [0] * (m + 1)

        for num, start, end in trips:
            prefix[start] += num
            if end + 1 < len(prefix):
                prefix[end] -= num
        print(prefix)
        for i in range(1, m+1):
            prefix[i] += prefix[i-1]
            if prefix[i-1] > capacity:
                return False
        return True
    