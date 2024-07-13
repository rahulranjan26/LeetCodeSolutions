class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        if k>len(nums):
            return -1
        # if k==len(nums):
        #     return max(nums)
        lo = max(nums)
        hi = sum(nums)
        ans = -1
        while lo<=hi:
            mid = (lo+hi)//2
            if self.findIfMinIsPossible(nums,k,mid)>k:
                lo = mid+1
            else:
                ans = mid
                hi=mid-1
        return ans
        


    def findIfMinIsPossible(self,nums,k,mid):
        workingSum = 0
        splits = 1
        for i in range(len(nums)):
            if workingSum+nums[i]<=mid:
                workingSum = workingSum+nums[i]
            else:
                workingSum = nums[i]
                splits+=1
        return splits

        