from collections import deque
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        visited = set()
        flag = False
        queue = deque()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]==1:
                    self.dfs(grid,row,col,visited,queue)
                    flag=True
                    break
            if flag:
                break
        ans = 0
        while queue:
            length = len(queue)
            for _ in range(length):  # Process entire level
                x,y = queue.popleft()
                for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                    xx, yy = x+dx, y+dy
                    if xx<0 or yy<0 or xx>=len(grid) or yy>=len(grid[0]) or (xx,yy) in visited:
                        continue
                    if grid[xx][yy]:
                        return ans
                    visited.add((xx,yy))
                    queue.append((xx,yy))
            ans += 1  # Increment ONCE per level

    def dfs(self,grid,row,col,visited,queue):
        if row<0 or col<0 or row>=len(grid) or col>=len(grid[0]) or (row,col) in visited or grid[row][col]==0:
            return 
        visited.add((row,col))
        queue.append((row,col))
        self.dfs(grid,row-1,col,visited,queue)
        self.dfs(grid,row,col-1,visited,queue)
        self.dfs(grid,row,col+1,visited,queue)
        self.dfs(grid,row+1,col,visited,queue)
        