# Problem: Flood Fill - https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        que = deque([(sr, sc)])
        d = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        starting_color = image[sr][sc]
        if starting_color == color:
            return image

        while que:
            
            r, c = que.popleft()
            image[r][c] = color
            for x, y in d:
                nx, ny = x + r, y + c
                if 0 <= nx < len(image) and 0 <= ny < len(image[0]) and image[nx][ny] == starting_color:
                    que.append((nx, ny))

        return image