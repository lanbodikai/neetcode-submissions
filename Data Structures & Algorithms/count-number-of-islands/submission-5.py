class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        row, col = len(grid), len(grid[0])
        visited = set()
        island = 0

        def bfs(r, c):
            queue = deque()
            visited.add((r, c))
            queue.append((r, c))

            directions = [
                (1, 0),
                (-1, 0),
                (0, 1),
                (0, -1)
            ]

            while queue:
                curr_row, curr_col = queue.popleft()

                for i , j in directions:
                    ni, nj = curr_row + i, curr_col + j

                    if (0 <= ni < row and 0 <= nj < col and grid[ni][nj] == "1" and (ni, nj) not in visited ):
                        visited.add((ni, nj))
                        queue.append((ni, nj))
            

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" and (i, j) not in visited:
                    bfs(i, j)
                    island += 1

        return island