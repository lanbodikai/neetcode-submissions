class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ma = {}
        freq = [[] for i in range(len(nums) + 1)]
        for i in nums:
            ma[i] = ma.get(i, 0) + 1
        

        
        for i, j in ma.items():
            freq[j].append(i)
        
        res = []

        for j in range(len(freq) - 1, 0, -1):
            for i in freq[j]:
                res.append(i)

                if len(res) == k:
                    return res