class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ans = 0
        j = 0
        i = 0
        
        while i<len(nums):
            if nums[i]==0:
                k=k-1
            if k<0:
                while k<0:
                    if nums[j]==0:
                        k=k+1
                    j = j+1
            ans = max(ans,i-j+1)
            i = i+1
        return ans
        