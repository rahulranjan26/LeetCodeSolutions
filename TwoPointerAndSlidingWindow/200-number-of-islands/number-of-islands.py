class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited=[[False]*len(grid[0]) for _ in range(len(grid))]
        count=0
        for i in range(len(grid)):
            print(1)
            for j in range(len(grid[0])):
                if grid[i][j]=='1' and visited[i][j] is False:
                    # print("indside loop")
                    self.dfs(grid,i,j,visited)
                    count+=1
        return count

    def dfs(self,grid,row,col,visited):
        if row<0 or col<0 or row>=len(grid) or col>=len(grid[0]) or visited[row][col] is True or grid[row][col]=='0':
            # print("inside return statement")
            return
        visited[row][col]=True
        # print("inside recursion")
        self.dfs(grid,row-1,col,visited)
        self.dfs(grid,row+1,col,visited)
        self.dfs(grid,row,col-1,visited)
        self.dfs(grid,row,col+1,visited)
        