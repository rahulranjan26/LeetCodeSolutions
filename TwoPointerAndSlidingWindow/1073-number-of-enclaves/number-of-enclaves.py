from collections import deque
from typing import List

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()

        # push all boundary 1s into queue and mark immediately
        for i in range(rows):
            for j in (0, cols-1):
                if grid[i][j] == 1:
                    q.append((i, j))
                    grid[i][j] = 0
        for j in range(cols):
            for i in (0, rows-1):
                if grid[i][j] == 1:
                    q.append((i, j))
                    grid[i][j] = 0

        # BFS to eliminate all border-connected lands
        while q:
            x, y = q.popleft()
            for dx, dy in ((-1,0),(1,0),(0,-1),(0,1)):
                nx, ny = x+dx, y+dy
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                    grid[nx][ny] = 0   # mark visited immediately
                    q.append((nx, ny))

        # count remaining enclaves
        return sum(grid[i][j] == 1 for i in range(rows) for j in range(cols))
