class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element in seen:
                    return False
                if element == ".":
                    continue
                else:
                    seen.add(element)
            seen.clear()
        
        for j in range(9):
            for i in range(9):
                element = board[i][j]
                if element in seen:
                    return False
                if element == ".":
                    continue
                else:
                    seen.add(element)
            seen.clear()
        
        for a in range(0, 9, 3):
            for b in range(0, 9, 3):
                for i in range(a, a + 3):
                    for j in range(b, b + 3):
                        element = board[i][j]

                        if element in seen:
                            return False

                        if element == ".":
                            continue
                        
                        seen.add(element)
                seen.clear()

        return True


