class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        seen = set()
        row, col = len(board), len(board[0])

        def dfs(i, x, y):
            if i == len(word):
                return True
            
            if x >= row or y >= col or x < 0 or y < 0:
                return False
            
            if (x, y) in seen:
                return False

            if board[x][y] != word[i]:
                return False
            
            
            seen.add((x, y))
            
            found = (
                dfs(i + 1, x + 1, y) or
                dfs(i + 1, x - 1, y) or
                dfs(i + 1, x, y + 1) or
                dfs(i + 1, x , y - 1)   
            )

            seen.remove((x ,y))

            return found
        
        for i in range(row):
            for j in range(col):
                if dfs(0, i, j):
                    return True
        return False
        
        


            
            