class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        for i in range(rows):
            for j in range(cols):
                top = grid[i-1][j] if i > 0 else float('inf')
                left = grid[i][j-1] if j > 0 else float('inf')

                if i == 0 and j == 0:
                    continue
                grid[i][j] += min(top, left)

        return grid[-1][-1]

        