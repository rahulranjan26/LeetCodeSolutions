class Solution:
    def maxDistance(self, positions: List[int], m: int) -> int:
        lo = 1
        hi = max(positions)-min(positions)
        positions.sort()
        ans = -1
        while lo<=hi:
            mid = (lo+hi)//2
            if self.canTheBallBePlaced(positions,m,mid):
                ans = mid
                lo = mid+1
            else:
                hi = mid-1
        return ans
        
    def canTheBallBePlaced(self,arr,m,dis):
        balls = 1
        lastPlaced = arr[0]
        
        for i in range(1,len(arr)):
            if arr[i]-lastPlaced>=dis:
                balls+=1
                lastPlaced = arr[i]
        
        return True if balls>=m else False
        
        