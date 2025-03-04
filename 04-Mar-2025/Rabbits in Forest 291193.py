# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count=Counter(answers)
        total_rabbit = 0

        for rab, freq in count.items():
            size = rab + 1
            group = (size + freq-1) // size
            total_rabbit += size * group
            
        return total_rabbit