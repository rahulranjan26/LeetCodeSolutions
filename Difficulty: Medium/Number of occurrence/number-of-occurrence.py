#User function Template for python3
class Solution:

	def count(self,nums, n, target):
		# code here
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
        if first!=-1 and last!=-1:
            return last-first+1
        return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.count(arr, n, x)
        print(ans)
        tc -= 1

# } Driver Code Ends