import heapq
class Solution:
    def minimumEffortPath(self, grid: List[List[int]]) -> int:
        queue = []
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        # queue = [grid[0][0],(0,0)]
        n = len(grid)
        m = len(grid[0])
        heapq.heappush(queue, (0, (0, 0)))

        while len(queue):
            cost, cords = heapq.heappop(queue)
            x = cords[0]
            y = cords[1]
            if x == n - 1 and y == m - 1:
                return cost
            if visited[x][y] == True:
                continue
            visited[x][y] = True

            for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                xx = x + dx
                yy = y + dy

                if xx < 0 or yy < 0 or xx >= n or yy >= m or visited[xx][yy] is True:
                    continue
                heapq.heappush(queue, (max(cost, abs(grid[xx][yy] - grid[x][y])), (xx, yy)))
        return None
        