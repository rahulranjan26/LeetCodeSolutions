class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        hashMap = {0:1}
        
        ans = 0
        prefix = 0
        for v in nums:
            prefix+=v
            ans+=hashMap.get(prefix-goal,0)
            hashMap[prefix]=hashMap.get(prefix,0)+1
        return ans