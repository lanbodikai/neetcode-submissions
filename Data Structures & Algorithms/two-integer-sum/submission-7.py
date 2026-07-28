class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}

        for i, e in enumerate(nums):
            d = target - e
            if d in s:
                return [s[d], i]
            else:
                s[e] = i
        
        return []