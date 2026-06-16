class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mins = 1
        maxs = max(piles)

        while mins < maxs:
            mid = (mins + maxs) // 2
            temp = 0
            for i in piles:
                temp += math.ceil(i/mid)
            if temp <= h:
                maxs = mid
            else:
                mins = mid + 1
        
        return mins
