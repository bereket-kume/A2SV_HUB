# Problem: Odd Even Linked List - https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = ListNode()
        even = ListNode()
        od_p = odd
        ev_p = even
        curr = head
        i = 1
        while curr:
            if i % 2 == 1:
                od_p.next = curr
                od_p = od_p.next
            else:
                ev_p.next = curr
                ev_p = ev_p.next
            i += 1
            curr = curr.next
        od_p.next = even.next
        ev_p.next = None
        return odd.next
        