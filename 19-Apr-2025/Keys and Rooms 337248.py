# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        que = deque()
        que.append(0)
        visited = set()
        visited.add(0)
        while que:
            current_room = que.popleft()
            for key in rooms[current_room]:
                if key not in visited:
                    visited.add(key)
                    que.append(key)
        return len(visited) == n