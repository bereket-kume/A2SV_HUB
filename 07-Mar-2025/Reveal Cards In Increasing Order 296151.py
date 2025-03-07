# Problem: Reveal Cards In Increasing Order - https://leetcode.com/problems/reveal-cards-in-increasing-order/



class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        deck.sort()
        position = deque(range(n))
        ans = [0] * n

        for card in deck:
            idx = position.popleft()
            ans[idx] = card

            if position:
                position.append(position.popleft())
                
        return ans