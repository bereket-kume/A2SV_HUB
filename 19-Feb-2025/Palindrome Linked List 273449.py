# Problem: Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []

        current = head

        while current:
            stack.append(current.val)
            current = current.next

        current = head
        while current:
            if current.val == stack[-1]:
                stack.pop()
            current = current.next

        return len(stack) == 0