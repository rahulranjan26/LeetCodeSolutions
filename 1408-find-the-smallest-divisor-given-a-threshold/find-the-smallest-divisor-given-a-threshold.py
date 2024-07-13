import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        lo = 1
        hi = sum(nums)
        ans = 0
        while lo<=hi:
            mid = (lo+hi)//2
            if self.divisorSumCheck(nums,threshold,mid):
                ans = mid
                hi = mid-1
            else:
                lo = mid+1
        return ans 
        
    def divisorSumCheck(self,nums,threshold, divisor):
        ans = 0
        for num in nums:
            ans = ans+ math.ceil(num/divisor)
        
        if ans<=threshold:
            return True
        return False
            