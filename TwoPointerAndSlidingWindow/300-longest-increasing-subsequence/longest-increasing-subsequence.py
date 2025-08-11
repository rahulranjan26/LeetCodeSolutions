class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []

        for n in nums:
            if not res or res[-1]<n:
                res.append(n)
            else:
                idx = self.binarySearch(res,n)
                res[idx]=n
        return len(res)
    


    def binarySearch(self,res,target):
        lo = 0
        hi = len(res)-1

        while lo<=hi:
            mid = (lo+hi)//2
            if res[mid]==target:
                return mid
            elif res[mid]>target:
                hi=mid-1
            else:
                lo=mid+1
        return lo

        