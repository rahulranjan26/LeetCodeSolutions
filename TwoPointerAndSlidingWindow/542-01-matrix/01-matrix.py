from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = deque()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==0:
                    queue.append([i,j])
                else:
                    mat[i][j]=-1
        
        while queue:
            x,y=queue.popleft()
            for dx,dy in [[-1,0],[1,0],[0,-1],[0,1]]:
                xx = x+dx
                yy = y+dy
                if 0<= xx<len(mat) and 0<= yy <len(mat[0]) and mat[xx][yy]<0:
                    mat[xx][yy]=mat[x][y]+1
                    queue.append([xx,yy])
        return mat
                    
        
        