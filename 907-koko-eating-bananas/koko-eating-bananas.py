import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo = 1
        hi = max(piles)
        
        ans = 0
        while lo<=hi:
            mid = (lo+hi)//2
            if self.eatingSpeedCheck(piles,h,mid):
                ans = mid
                hi = mid-1
            else:
                lo = mid+1
        return ans
        
    def eatingSpeedCheck(self,piles,h,speed):
        hours = 0
        
        for i in range(len(piles)):
            hours=hours+math.ceil(piles[i]/speed)
            
        if hours<=h:
            return True
        return False
            
        