#User function Template for python3


#Complete this function
class Solution:
    def floorSqrt(self, x): 
    #Your code here
    
        lo = 1
        hi = x
        ans = 0
        while lo<=hi:
            mid = (lo+hi)//2
            if mid*mid==x:
                return mid
            elif mid*mid < x:
                ans = mid
                lo = mid+1
            else:
                hi = mid-1
        return ans
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            x=int(input())
            
            print(Solution().floorSqrt(x))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends