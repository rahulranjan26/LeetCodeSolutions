#User function Template for python3

class Solution:
    def solve(self,n,k,positions):
        lo = 1
        hi = max(positions)-min(positions)
        positions.sort()
        ans = -1
        while lo<=hi:
            mid = (lo+hi)//2
            if self.canTheBallBePlaced(positions,k,mid):
                ans = mid
                lo = mid+1
            else:
                hi = mid-1
        return ans
        
    def canTheBallBePlaced(self,arr,m,dis):
        balls = 1
        lastPlaced = arr[0]
        
        for i in range(1,len(arr)):
            if arr[i]-lastPlaced>=dis:
                balls+=1
                lastPlaced = arr[i]
        
        return True if balls>=m else False
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n, k = list(map(int, input().split()))
        stalls = list(map(int, input().split()))
        ob = Solution()
        res = ob.solve(n, k, stalls)
        print(res)

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends