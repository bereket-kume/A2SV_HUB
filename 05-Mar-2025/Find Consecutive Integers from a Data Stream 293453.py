# Problem: Find Consecutive Integers from a Data Stream - https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/

class DataStream:

    def __init__(self, value: int, k: int):
        self.value=value
        self.k=k
        self.queue = deque()
        self.count = 0

    def consec(self, num: int) -> bool:
        self.queue.append(num)
        if num == self.value:
            self.count += 1
        

        if len(self.queue) > self.k:
            removed = self.queue.popleft()
            if removed == self.value:
                self.count -= 1
                
        if self.count >= self.k:
            return True
        return False



# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)