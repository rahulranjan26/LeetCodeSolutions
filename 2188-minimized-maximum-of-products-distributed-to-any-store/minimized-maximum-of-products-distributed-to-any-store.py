import math
class Solution:
    def minimizedMaximum(self, m: int, positions: List[int]) -> int:
        if len(positions)==1:
            return math.ceil(positions[0]/m)
        lo = 1
        hi = max(positions)
        # positions.sort()
        ans = -1
        while lo<=hi:
            mid = (lo+hi)//2
            if self.canTheBallBePlaced(positions,m,mid):
                ans = mid
                hi = mid-1
            else:
                
                lo = mid+1
        return ans
        
    def canTheBallBePlaced(self,arr,m,dis):
        temp = 0
        for ar in arr:
            temp = temp+math.ceil(ar/dis)
        if temp > m:
            return False
        return True

        