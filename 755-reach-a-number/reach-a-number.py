import math
class Solution:
    def reachNumber(self, target: int) -> int:
        num = math.ceil((math.sqrt(8*abs(target) + 1) - 1)/2)
        while True:
            if ((num*(num + 1))/2 - target) %2 != 0: 
                num+=1
            else: 
                return num
#     ```
#     Intuition
# Approach
# target = abs(target)
# The direction to the target (left or right) doesn't really matter because moving to a positive target t would take the same number of moves as moving to its negative -t due to the symmetric nature of the number line. So, we can always consider the target as positive.

# n, sum_n = 0, 0
# We initialize two variables:

# n represents the number of moves made.
# sum_n is the cumulative sum of the moves made. It represents the total distance covered in n moves if we only move right.

# while sum_n < target or (sum_n - target) % 2 != 0:
#     n += 1
#     sum_n += n
# We need to keep moving until two conditions are met:

# The total distance covered (sum_n) is at least the target.
# The difference between sum_n and the target is even. This is because, to adjust our position to land exactly on the target, we may need to switch some of the rightward steps to leftward steps. Switching a rightward step of size i to a leftward one changes our position by -2i (because we lose i steps in the rightward direction and gain i in the leftward one). This operation always changes our position by an even number, hence the requirement for (sum_n - target) % 2 to be even.

# return n
# After exiting the loop, n will contain the minimum number of moves required to reach the target, so we return it.

# Complexity
# Time complexity:
# O(n^2)

# Space complexity:
# O(1)

            