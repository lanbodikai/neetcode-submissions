class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        n = len(nums) - 1
        while i <= n:
            start = nums[i]
            end = nums[n]

            mid = (i + n) // 2
            if target < nums[mid]:
                n = mid - 1
            elif target > nums[mid]:
                i = mid + 1
            else:
                return mid
        
        return -1
