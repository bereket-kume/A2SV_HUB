# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k=len(s1)
        m=len(s2)
        count_one=Counter(s1)
        count_two=Counter(s2[:k])
        left = 0
        if count_one == count_two:
            return True

        for i in range(k, m):
            count_two[s2[left]] -= 1
            count_two[s2[i]] += 1

            if count_two[s2[left]] == 0:
                del count_two[s2[left]]
            left += 1

            if count_one == count_two:
                return True
        
        return False