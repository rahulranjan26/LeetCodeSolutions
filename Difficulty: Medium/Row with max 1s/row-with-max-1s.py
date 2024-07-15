#User function Template for python3
class Solution:

	def rowWithMax1s(self,arr, n, m):
		# code here
		i = 0
		j = m-1
		count=0
		res = 0
		
		while i<n and j>=0:
		    if arr[i][j]==1:
		        j = j-1
	        else:
	            if count < m-j-1:
	                count = m-j-1
	                res = i
	            i = i+1
	            j =m-1
	    
	    if i!=n:
	        return i
	    if count ==0:
	        return -1
	    return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = list(map(int, input().strip().split()))
        
        inputLine = list(map(int, input().strip().split()))
        arr = [[0 for j in range(m)] for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                arr[i][j] = inputLine[i * m + j]
        ob = Solution()
        ans = ob.rowWithMax1s(arr, n, m)
        print(ans)
        tc -= 1

# } Driver Code Ends