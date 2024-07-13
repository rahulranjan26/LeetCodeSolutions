#User function Template for python3

class Solution:
	def NthRoot(self, n, m):
		# Code here
		lo = 1
		hi = m
		
		while lo<=hi:
		    mid = (lo+hi)//2
		    val = mid ** (n)
		    if val == m:
		        return mid
	        elif val < m:
	            lo = mid+1
            else:
                hi = mid -1
        return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n); m = int(m);
		ob = Solution()
		ans = ob.NthRoot(n, m)
		print(ans)
# } Driver Code Ends