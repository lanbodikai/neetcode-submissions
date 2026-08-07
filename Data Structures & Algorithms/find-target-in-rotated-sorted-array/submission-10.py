class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        n = len(nums) - 1

        while i <= n:
            mid = (i + n)//2
            if nums[mid] == target:
                return mid

            if nums[mid] > nums[n]:
                if nums[i] <= target < nums[mid]:
                    n = mid - 1
                else:
                    i = mid + 1
            else:
                if nums[mid] < target <= nums[n]:
                    i = mid + 1
                else:
                    n = mid - 1
        
        return -1
            