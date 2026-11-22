class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        long = 0
        count = 1
        nums.sort()

        for i in range(len(nums))[1:]:
            if nums[i] == nums[i - 1] + 1:
                count += 1
            elif nums[i] == nums[i - 1]:
                continue
            else:
                long = max(long, count)
                count = 1
        
        long = max(long, count)

        return long