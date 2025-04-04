# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        carry = 0
        def solve(l1, l2, carry):
            nonlocal current
            if not l1 and not l2 and not carry:
                return 
                
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            total = v1 + v2 + carry
            carry = total // 10
            total = total % 10
            new_node = ListNode(total)
            current.next = new_node
            current = current.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            solve(l1, l2, carry)

        solve(l1, l2, 0)
        return dummy.next
