class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay)<m*k:
            return -1
        lo = min(bloomDay)
        hi = max(bloomDay)
        ans = 0
        while lo<=hi:
            mid = (lo+hi)//2
            if self.bouquetsMakingCheck(bloomDay,m,k,mid)>=m:
                ans = mid
                hi = mid-1
            else:
                lo = mid+1
        return ans
    
    def bouquetsMakingCheck(self,bloomDay,m,k,mid):
        num_of_bouquets = 0
        count = 0

        for day in bloomDay:
            # If the flower is bloomed, add to the set. Else reset the count.
            if day <= mid:
                count += 1
            else:
                count = 0

            if count == k:
                num_of_bouquets += 1
                count = 0

        return num_of_bouquets
        
        