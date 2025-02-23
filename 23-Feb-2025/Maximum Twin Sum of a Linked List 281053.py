# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        prev = None
        current = slow
        while current:
            tmp = current.next
            current.next = prev
            prev = current
            current = tmp

        ans = 0
       
        while prev:
            ans = max(ans, prev.val + head.val)
            prev = prev.next
            head = head.next
        return ans
