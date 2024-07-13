import math
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left = 1
        right = max(piles)
        result = right
        
        while left <= right:
            k = (left + right) // 2
            hours = 0
            
            for pile in piles:
                hours += math.ceil(pile / k)

            if hours <= h:
                result = min(result, k)
                right = k - 1
            else:
                left = k + 1


        return  result


piles = [3,6,7,11]
h = 8
print(Solution().minEatingSpeed(piles, h))


        