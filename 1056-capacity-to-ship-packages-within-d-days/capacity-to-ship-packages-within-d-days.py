class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        lo = max(weights)
        hi = sum(weights)
        ans = 0
        while lo<=hi:
            mid = (lo+hi)//2
            if self.checkForDays(weights,mid,days):
                hi = mid-1
                ans = mid
            else:
                lo = mid+1
        
        return ans
    
    def checkForDays(self, weights, target, targetDays):
        days = 1
        wt = 0
        
        for i in range(0,len(weights)):
            wt = wt+weights[i]
            
           
            
            if wt > target:
                days=days+1
                wt = weights[i]
        
        if days<=targetDays:
            return True
        return False
                
        