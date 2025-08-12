class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        dpf = self.findLIS(nums)
        dpb = self.findLIS(nums[::-1])[::-1]

        x = 0
        for i in range(len(dpf)):
            if dpf[i]>1 and dpb[i]>1:
                x = max(x, dpf[i]+dpb[i])
        print(dpf,dpb,x)
        # print(x,len(nums)-x+1)
        return len(nums)-x+1
    

    def findLIS(self,nums):
        dp = [1]*len(nums)

        for i in range(0, len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i]=max(dp[i],dp[j]+1)
        return dp
    

    def findLDS(self,nums):
        dp = [1]*len(nums)

        for i in range(len(nums)-1, -1,-1):
            for j in range(i+1,len(nums)):
                if nums[i]>nums[j]:
                    dp[i]=max(dp[i],dp[j]+1)
        return dp


    


    def findIdx(self,res,x):

        lo = 0
        hi - len(res)-1

        while lo<=hi:
            mid=(lo+hi)//2
            if res[mid]==x:
                return mid
            elif res[mid]>x:
                hi=mid-1
            else:
                lo=mid+1
        return lo
        