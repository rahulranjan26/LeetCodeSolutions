class Solution:
    def search(self, arr: List[int], target: int) -> bool:
        lo = 0
        hi = len(arr)-1

        while lo<=hi:
            mid = (lo+hi)//2

            if arr[mid]==target:
                return True
#             Shrink the seach space
            if arr[lo]==arr[mid] and arr[hi]==arr[mid]:
                lo = lo+1
                hi = hi-1
                continue

            if arr[lo]<=arr[mid]:
                if target >= arr[lo] and target < arr[mid]:
                    hi = mid-1
                else:
                    lo = mid+1
            else:
                if target > arr[mid] and target <= arr[hi]:
                    lo = mid+1
                else:
                    hi = mid-1
        
        return False
        