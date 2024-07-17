import sys
class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        lo = min(nums)
        hi = max(nums)
    
        while lo<=hi:
            mid = (lo+hi)//2
            if self.findMax(nums,mid,k):
                hi = mid-1
            else:
                lo = mid+1
        return lo
            
    
    def findMax(self,nums,mid,k):
        i = 0
        while i<len(nums):
            if nums[i]<=mid:
                i+=2
                k-=1
            else:
                i = i+1
            
            if k==0:
                return True
            
        
        return False



        