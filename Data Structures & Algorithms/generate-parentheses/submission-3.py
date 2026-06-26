class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        temp = ""
        def dfs(temp, o, c):

            if len(temp) == 2 * n:
                res.append(temp)
                return
            if o < n:
                dfs(temp + "(", o + 1, c)
            if c < o:
                dfs(temp + ")", o, c + 1)
        dfs("",0,0)
        return res