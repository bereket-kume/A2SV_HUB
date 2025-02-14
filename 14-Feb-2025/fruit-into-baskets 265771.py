# Problem: fruit-into-baskets - https://leetcode.com/problems/fruit-into-baskets/

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        count = defaultdict(int)

        left, right = 0, 0
        ans = 0

        while right < len(fruits):
            count[fruits[right]] += 1

            while len(count) > 2:
                count[fruits[left]] -= 1
                if count[fruits[left]] == 0:
                    del count[fruits[left]]
                left += 1
            ans = max(ans, right-left + 1)
            right += 1
        return ans