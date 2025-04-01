# Problem: Sort List - https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def find_middle(node):
            slow, fast = node, node.next

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            
            return slow
        
        def merge(l1, l2):
            dummy = ListNode()
            tail = dummy

            while l1 and l2:
                if l1.val < l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next

                tail = tail.next
            tail.next = l1 if l1 else l2
            return dummy.next
        def merge_sort(head):
            if not head or not head.next:
                return head
            
            middle = find_middle(head)
            right_half = middle.next
            middle.next = None

            left_sorted = merge_sort(head)
            right_sorted = merge_sort(right_half)
            return merge(left_sorted, right_sorted)
        return merge_sort(head)