"""
if u have speed
and multiple piles of p bananas
to calculate total hours need

for each pile:
    ceiling of (bananas/hr)/p
"""
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # speed 1 to max speed 
        l = 1
        r = max(piles)
        
        res = r

        while l <= r:
            k = (l+r) // 2

            total_hours = 0
            for p in piles:
                total_hours += math.ceil(p/k)
            if total_hours <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res
