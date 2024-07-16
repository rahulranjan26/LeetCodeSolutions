class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        s = ""
        ans = []
        for i in range(len(searchWord)):
            s+=searchWord[i]
            idx = self.findTheFirstIndex(products,s)
            temp = []
            for x in range(idx, min(len(products),idx+3)):
                if products[x][:i+1]==s:
                    temp.append(products[x])
            ans.append(temp)
        return ans
    
    
    def findTheFirstIndex(self,products,s):
        lo = 0
        hi = len(products)-1
        
        while lo<=hi:
            mid = (lo+hi)//2
            if products[mid]<s:
                lo = mid+1
            else:
                hi = mid-1
        return lo
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         products.sort()
        
#         ans = []
#         for i in range(len(searchWord)):
#             patt = searchWord[:i+1]
#             temp = self.findIndex(products,patt,i)
#             ans.append(temp[:3])
#         return ans
    
    
#     def findIndex(self,products,patt,idx):
#         ans = []
#         for i in range(len(products)):
#             if patt==products[i][:idx+1]:
#                 ans.append(products[i])
#         return ans
        
            
        