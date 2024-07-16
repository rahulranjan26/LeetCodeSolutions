class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        
        ans = []
        for i in range(len(searchWord)):
            patt = searchWord[:i+1]
            temp = self.findIndex(products,patt,i)
            ans.append(temp[:3])
        return ans
    
    
    def findIndex(self,products,patt,idx):
        ans = []
        
        for i in range(len(products)):
            if patt==products[i][:idx+1]:
                ans.append(products[i])
        return ans
        
            
        