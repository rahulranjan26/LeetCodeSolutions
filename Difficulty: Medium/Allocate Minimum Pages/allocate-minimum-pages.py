class Solution:
    
    #Function to find minimum number of pages.
    def findPages(self,n ,nums ,k):
        #code here
        if k>len(nums):
            return -1
        # if k==len(nums):
        #     return max(nums)
        lo = max(nums)
        hi = sum(nums)
        ans = -1
        while lo<=hi:
            mid = (lo+hi)//2
            if self.findIfMinIsPossible(nums,k,mid)>k:
                lo = mid+1
            else:
                ans = mid
                hi=mid-1
        return ans
        


    def findIfMinIsPossible(self,nums,k,mid):
        workingSum = 0
        splits = 1
        for i in range(len(nums)):
            if workingSum+nums[i]<=mid:
                workingSum = workingSum+nums[i]
            else:
                workingSum = nums[i]
                splits+=1
        return splits




#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        n = int(input())

        arr = [int(x) for x in input().strip().split()]
        m = int(input())

        ob = Solution()

        print(ob.findPages(n, arr, m))

# } Driver Code Ends