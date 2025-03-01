# Problem: Reverse Linked List II - https://leetcode.com/problems/reverse-linked-list-ii/

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode()
        dummy.next = head
        prev = dummy

        for _ in range(left-1):
            prev = prev.next
        start = prev.next
        

        current = start

        for _ in range(right - left):
            current = current.next
        
        end = current.next
        current.next = None

        p=None

        while start:
            next_node = start.next
            start.next = p
            p = start
            start = next_node
        prev.next = p

        while p.next:
            p = p.next
        p.next = end

        return dummy.next