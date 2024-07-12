class Solution:
    def hIndex(self, citations: List[int]) -> int:
        lo = 0
        hi = len(citations)-1
        
        n = len(citations)
        
        while lo<=hi:
            mid = (lo+hi)//2
            
            if citations[mid]>=n-mid:
                hi = mid-1
            else:
                lo = mid+1
        
        return n-lo
        