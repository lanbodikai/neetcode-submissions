class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        here = {}
        res = []
        calc = []

        candidates.sort()
        
        def dfs(i):
            if sum(calc) == target:
                res.append(calc.copy())
                return
            
            if sum(calc) > target or i == len(candidates):
                return

            
            calc.append(candidates[i])
            dfs(i + 1)

            calc.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1] :
                i += 1

            dfs(i + 1)
        dfs(0)
        return res