import math
class Solution:
    def repairCars(self, ranks, cars):
        lo = 1
        hi = cars * cars * max(ranks)
        ans = -1
        while lo <= hi:
            mid = (hi + lo) // 2
            if self.isPossible(ranks, cars, mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return ans

    def isPossible(self, ranks, cars, mid):
        totalCars = 0
        for i in range(len(ranks)):
            totalCars = totalCars + math.floor(math.sqrt(mid // ranks[i]))
            if totalCars >= cars:
                return True
        return False

        
            