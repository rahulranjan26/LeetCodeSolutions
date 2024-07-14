class Solution:
    #User function Template for python3
    
    #Complete this function
    def findFloor(self,arr,n,x):
        #Your code here
        if x<arr[0]:
            return -1
        if x>arr[-1]:
            return len(arr)-1
        
        lo = 0
        hi = len(arr)-1
        
        while lo<=hi:
            mid = (lo+hi)//2
            if arr[mid]==x:
                return mid
            elif arr[mid]>x:
                hi = mid-1
            else:
                lo = mid+1
        
        return hi
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        NX = [int(x) for x in input().strip().split()]
        N = NX[0]
        X = NX[1]

        A = [int(x) for x in input().strip().split()]

        obj = Solution()
        print(obj.findFloor(A, N, X))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends