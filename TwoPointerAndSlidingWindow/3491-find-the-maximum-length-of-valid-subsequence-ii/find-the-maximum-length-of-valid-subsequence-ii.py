class Solution:
    def maximumLength(self, nums, k):
        dp = [[0] * (k + 1) for _ in range(len(nums))]
        ans = 0

        for i in range(len(nums)):
            for j in range(i):
                t = (nums[i] + nums[j]) % k
                dp[i][t] = dp[j][t] + 1
                ans = max(ans, dp[i][t])

        return ans + 1



        