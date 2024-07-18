class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        res = []
        prefix= 0
        prefixSum = []
        for i in range(len(nums)):
            prefix = prefix+nums[i]
            prefixSum.append(prefix)
            res.append(prefix)
        for i in range(0,len(prefixSum)):
            temp = prefixSum[i]
            for j in range(i+1,len(prefixSum)):
                pre = prefixSum[j]-temp
                res.append(pre)
        res.sort()
        # print(res)
        return sum(res[left-1:right])%1000000007
        