import math
class Solution:
    def reachNumber(self, target: int) -> int:
        num = math.ceil((math.sqrt(8*abs(target) + 1) - 1)/2)
        while True:
            if ((num*(num + 1))/2 - target) %2 != 0: 
                num+=1
            else: 
                return num
            