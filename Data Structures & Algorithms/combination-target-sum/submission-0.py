class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        calc = []
        res = []
        def dfs(i):
            if sum(calc) == target:
                res.append(calc.copy())
                return
            elif sum(calc) > target:
                return
            
            if i == len(nums):
                return
            
            calc.append(nums[i])
            dfs(i)

            calc.pop()
            dfs(i + 1)
        dfs(0)

        return res