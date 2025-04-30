class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = []
        for row in triangle:
            
            temp = len(row)
            temp2 = []
            for i in range(temp):
                temp2.append(0)
            dp.append(temp2)
        for i in range(len(dp)-1,-1,-1):
            for j in range(len(dp[i])-1,-1,-1):
                if i==len(dp)-1:
                    dp[i][j] = triangle[i][j]
                else:
                    target1 = dp[i+1][j]
                    target2 = dp[i+1][j+1]
                    dp[i][j] = min(triangle[i][j]+target1,triangle[i][j]+target2)
        return dp[0][0]


        