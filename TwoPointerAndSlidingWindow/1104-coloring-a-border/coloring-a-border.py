class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        self.bfs(grid,row,col,color)
        return grid

    def bfs(self,grid, row, col, color):
        queue = [[row, col]]
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        val = grid[row][col]
        while queue:
            size = len(queue)
            while size > 0:
                x, y = queue.pop(0)
                visited[x][y] = True
                grid[x][y] = -val

                for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and visited[nx][ny] is False and abs(
                            grid[nx][ny]) == val:
                        queue.append([nx, ny])

                if (
                        (self.isValid(grid, x - 1, y) and abs(grid[x][y]) == abs(grid[x - 1][y])) and
                        (self.isValid(grid, x + 1, y) and abs(grid[x][y]) == abs(grid[x + 1][y])) and
                        (self.isValid(grid, x, y - 1) and abs(grid[x][y]) == abs(grid[x][y - 1])) and
                        (self.isValid(grid, x, y + 1) and abs(grid[x][y]) == abs(grid[x][y + 1]))
                ):
                    grid[x][y] = abs(grid[x][y])
                size -= 1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] < 0:
                    grid[i][j] = color

    
    def isValid(self,grid, row, col):
        if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
            return True
        return False

        