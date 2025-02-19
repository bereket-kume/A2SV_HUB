# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class ListNode:
    def __init__(self, value=0, next=None):
        self.val = value
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        current = self.head

        for _ in range(index):
            current = current.next
        return current.val


    def addAtHead(self, val: int) -> None:
        new_val = ListNode(val)
        new_val.next = self.head
        self.head = new_val
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_val = ListNode(val)
        if not self.head:
            self.head = new_val
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_val
        self.size += 1

        

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        
        new_node = ListNode(val)
        
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
        
        self.size += 1
        
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(index-1):
                current = current.next
            if current.next:
                current.next = current.next.next
        self.size -= 1
        
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)