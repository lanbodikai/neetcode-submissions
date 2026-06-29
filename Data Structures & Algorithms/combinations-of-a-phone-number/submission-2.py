class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        ma = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }
        res = []
        temp = []

        def dfs(i):
            if i == len(digits):
                res.append("".join(temp))
                return
            
            digit = digits[i]

            for char in ma[digit]:
                temp.append(char)
                dfs(i + 1)
                temp.pop()

        dfs(0)
        return res

            
