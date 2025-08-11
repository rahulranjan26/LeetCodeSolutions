import collections
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [1]*len(nums)
        count=[1]*len(nums)
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    if dp[i]<dp[j]+1:
                        dp[i] = dp[j] + 1
                        count[i]=count[j]
                    elif dp[i]==dp[j]+1:
                        count[i]+=count[j]
        
        max_len = max(dp)
        total = 0
        for i in range(len(nums)):
            if dp[i] == max_len:
                total += count[i]
        return total