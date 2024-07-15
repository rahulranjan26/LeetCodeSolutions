class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lo = 0
        hi = len(matrix[0])-1
        
        while lo<len(matrix) and hi>=0:
            val = matrix[lo][hi]
            if val==target:
                return True
            elif val>target:
                hi = hi-1
            else:
                lo = lo+1
        return False
        