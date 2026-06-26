class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        here = {}
        res = []
        calc = []

        candidates.sort()
        
        def dfs(i, total):
            if total == target:
                res.append(calc.copy())
                return
            
            if i == len(candidates) or total + candidates[i] > target:
                return

            
            calc.append(candidates[i])
            dfs(i + 1, total + candidates[i])

            calc.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1] :
                i += 1

            dfs(i + 1, total)
        dfs(0, 0)
        return res