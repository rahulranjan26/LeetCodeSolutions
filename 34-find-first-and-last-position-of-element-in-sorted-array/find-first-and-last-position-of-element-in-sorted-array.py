class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = -1
        last = -1
        
        lo = 0
        hi = len(nums)-1
        
        while lo<=hi:
            mid = (lo+hi)//2
            
            if(nums[mid]==target):
                first = mid
                hi = mid-1
            elif nums[mid]<target:
                lo = mid+1
            else:
                hi = mid-1
        
        
        lo = 0
        hi = len(nums)-1
        
        while lo<=hi:
            mid = (lo+hi)//2
            
            if(nums[mid]>target):
                hi = mid-1
            elif nums[mid]==target:
                last = mid
                lo = mid+1
            else:
                lo = mid+1
        
        return [first,last]
                
        