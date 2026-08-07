class Solution:
    def findMin(self, nums: List[int]) -> int:
        i = 0
        n = len(nums) - 1
        minv = float('inf')

        while i < n:
            mid = (n + i)//2
            minv = min(minv, nums[mid])


            if nums[mid] > nums[n]: #in right half
                i = mid + 1
            else: 
                n = mid
            
        
        return min(minv, nums[i])