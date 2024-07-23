class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        i = 0
        j = 0
        ans = 0
        
        while i<len(s):
            if s[i] in hashmap:
                if hashmap[s[i]] >= j:
                    j = hashmap[s[i]]+1
            ans = max(ans,i-j+1)
            hashmap[s[i]]=i
            i=i+1
        return ans
        