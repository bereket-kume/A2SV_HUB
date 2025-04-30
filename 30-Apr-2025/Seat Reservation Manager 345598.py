# Problem: Seat Reservation Manager - https://leetcode.com/problems/seat-reservation-manager/description/

class SeatManager:

    def __init__(self, n: int):
        self.heap = list(range(1, n+1))
        heapq.heapify(self.heap)

    def reserve(self) -> int:
        val = heapq.heappop(self.heap)
        return val
        
    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.heap, seatNumber)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)