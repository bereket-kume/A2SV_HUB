# Problem: Reverse Nodes in k-Group - https://leetcode.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        gprev = dummy

        while True:
            kth = self.getkth(gprev, k)

            if not kth:
                break
            grnext = kth.next

            prev, curr = grnext, gprev.next

            while curr != grnext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = gprev.next
            gprev.next = kth
            gprev = tmp

        return dummy.next

    def getkth(self, cur, k):
        while cur and k > 0:
            cur = cur.next
            k -= 1
        return cur