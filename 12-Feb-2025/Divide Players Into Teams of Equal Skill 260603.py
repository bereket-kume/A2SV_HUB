# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()

        left, right = 0, len(skill)-1
        ans = 0
        target = skill[left] + skill[right]
        while left < right:

            if skill[left] + skill[right] != target:
                return -1
            ans += skill[left] * skill[right]
            left += 1
            right -= 1
            
        return ans
