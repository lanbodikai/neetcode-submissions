class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        maxcount = 0
        count = 1
        for i in range(1, len(nums)):
            if nums[i] - 1 == nums[i - 1]:
                count += 1
            elif nums[i] == nums[i - 1]:
                continue
            else:
                maxcount = max(maxcount, count)
                count = 1

        return max(maxcount, count)