class Solution:
    def findMin(self, nums: List[int]) -> int:
        i = 0
        n = len(nums) - 1

        while i < n:
            mid = (n + i)//2

            if nums[mid] > nums[n]: #in right half
                i = mid + 1
            else: 
                n = mid
            
        
        return nums[i]