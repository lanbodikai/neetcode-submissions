class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        temp = []
        def palindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def dfs(i):
            if i == len(s):
                res.append(temp.copy())
                return

            for j in range(i, len(s)):
                if palindrome(i, j):
                    temp.append(s[i: j + 1])
                    dfs(j + 1)
                    temp.pop()
        
        dfs(0)
        return res

