# Problem: Merge k Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        count = 0

        for node in lists:
            if node:
                heapq.heappush(heap, (node.val,count, node))
                count += 1

        dummy = ListNode()
        current = dummy

        while heap:
            _,_, node = heapq.heappop(heap)
            current.next = node
            current = current.next

            if node.next:
                heapq.heappush(heap, (node.next.val,count, node.next))
                count += 1
        return dummy.next