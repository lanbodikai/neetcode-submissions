class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        n = len(heights) - 1
        maxval = 0

        while i < n:
            val = min(heights[i], heights[n]) * (n - i)
            maxval = max(maxval, val)

            if heights[i] < heights[n]:
                i += 1
            else:
                n -= 1
        
        return maxval

            