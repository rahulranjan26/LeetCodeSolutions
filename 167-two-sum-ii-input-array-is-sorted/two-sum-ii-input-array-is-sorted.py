class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lo = 0
        hi = len(numbers)-1
        
        while lo<hi:
            val = numbers[lo]+numbers[hi]
            if val == target:
                return [lo+1,hi+1]
            elif val>target:
                hi = hi-1
            else:
                lo = lo+1
        
        