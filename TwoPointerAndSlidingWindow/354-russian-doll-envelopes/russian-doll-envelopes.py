class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key = lambda x : (x[0], -x[1]))
        dp = []
        
        for _,h in envelopes :
            if not dp or dp[-1] < h : 
                dp.append(h) 
            else :
                idx = bisect_left(dp, h)  #finds inserting idx.
                dp[idx] = h
        return len(dp)
        