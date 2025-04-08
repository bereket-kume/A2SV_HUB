# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        in_deger = [0] * (n + 1)
        out_deger = [0] * (n+1)

        for give, reciver in trust:
            in_deger[give] += 1
            out_deger[reciver] +=1
        
        
        for i in range(1,n+1):
            if in_deger[i] == 0 and out_deger[i] == n - 1:
                return i
                
        return -1