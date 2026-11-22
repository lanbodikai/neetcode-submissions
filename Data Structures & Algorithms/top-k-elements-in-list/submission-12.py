class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countmap = {}
        res = []

        for i in nums:
            countmap[i] = countmap.get(i, 0) + 1
        
        sort = sorted(countmap, key=countmap.get, reverse = True)

        return sort[:k]