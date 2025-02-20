# Problem: Partition List - https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        current = head
        first_half = ListNode()
        second_half = ListNode()

        first_end = first_half
        second_end = second_half

        while current:
                if current.val < x:
                    first_end.next = current
                    
                    first_end = first_end.next
                else:
                    second_end.next = current
                    second_end = second_end.next
                current = current.next
                
        first_end.next = second_half.next
        second_end.next = None

        return first_half.next