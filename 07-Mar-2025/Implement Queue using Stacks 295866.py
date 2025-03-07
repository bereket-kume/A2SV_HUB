# Problem: Implement Queue using Stacks - https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        self.arr = deque()

    def push(self, x: int) -> None:
        self.arr.append(x)
        

    def pop(self) -> int:
       pop = self.arr.popleft()
       return pop
        

    def peek(self) -> int:
        peek = self.arr[0]
        return peek
        

    def empty(self) -> bool:
        if not self.arr:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()