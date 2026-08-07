class Solution:
    def findMin(self, nums: List[int]) -> int:
        i = 0
        n = len(nums) - 1
        minv = float('inf')

        while i < n:
            mid = (n + i)//2

            if nums[mid] > nums[n]: #in right half
                minv = min(minv, nums[n])
                i = mid + 1
            else: 
                minv = min(minv, nums[mid])
                n = mid
            
        
        return min(minv,nums[i])