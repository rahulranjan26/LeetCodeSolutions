class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        answer = 0
        counts = {0: 0, 1: 0}
        
        for right, num in enumerate(nums):
            counts[num] += 1
            
            while counts[0] > k:
                counts[nums[left]] -= 1
                left += 1
                
            curr_window_size = right - left + 1
            answer = max(answer, curr_window_size)
            
        return answer
#         ans = 0
#         j = 0
#         i = 0
        
#         while i<len(nums):
#             if nums[i]==0:
#                 k=k-1
#             if k<0:
#                 while k<0:
#                     if nums[j]==0:
#                         k=k+1
#                     j = j+1
#             ans = max(ans,i-j+1)
#             i = i+1
#         return ans
        