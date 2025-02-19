# Problem: Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse(head):
            current = head
            prev = None
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev

        slow=fast=head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        first_half = head
        second_half = reverse(slow)

        while second_half:
            if first_half.val != second_half.val:
                return False
            first_half = first_half.next
            second_half = second_half.next

        return True