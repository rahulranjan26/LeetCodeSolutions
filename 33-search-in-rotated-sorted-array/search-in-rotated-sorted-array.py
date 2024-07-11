class Solution:
    def search(self, arr: List[int], target: int) -> int:
        lo = 0
        hi = len(arr)-1

        while lo<=hi:
            mid = (lo+hi)//2

            if arr[mid]==target:
                return mid

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
        
        return -1
            
            



        