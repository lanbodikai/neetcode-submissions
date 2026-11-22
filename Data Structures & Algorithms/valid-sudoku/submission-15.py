class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r = len(board)
        c = len(board[0])
        for i in range(r):
            seen_row = set()
            for j in range(c):
                element = board[i][j]
                if element not in seen_row:
                    if element != ".":
                        seen_row.add(element)
                    else:
                        continue
                else:
                    return False
        for i in range(r):
            seen_col = set()
            for j in range(c):
                element = board[j][i]
                if element not in seen_col:
                    if element != ".":
                        seen_col.add(element)
                    else:
                        continue
                else:
                    return False
        
        for i in range(0, r, 3):
            for j in range(0, c, 3):
                seen_grid = set()
                for ro in range(i, i+3):
                    for co in range(j, j+3):
                        element = board[ro][co]
                        if element not in seen_grid:
                            if element != ".":
                                seen_grid.add(element)
                            else:
                                continue
                        else:
                            return False

        return True

