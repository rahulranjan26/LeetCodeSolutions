class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        lo = 0
        hi = len(arr)-1
        
        while lo<=hi:
            mid = (lo+hi)//2
            if arr[mid]-mid-1<k:
                lo = mid+1
            else:
                hi = mid-1
        
        return hi+k+1