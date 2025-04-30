class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        dp = [[0]*len(matrix) for i in range(len(matrix))]

        dp[0] = matrix[0]
        for i in range(1,len(matrix)):
            for j in range(len(matrix)):
                left = dp[i-1][j-1] if j>0 else float('inf')
                mid = dp[i-1][j]
                right = dp[i-1][j+1] if j+1 < len(matrix) else float('inf')
                dp[i][j] = matrix[i][j] + min(left,mid,right)
        return min(dp[-1])
        