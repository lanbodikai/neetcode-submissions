class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        row, col = len(grid), len(grid[0])

        max_count = 0
        seen = set()
        count = 0
        def bfs(r, c):
            queue = deque()
            seen.add((r,c))
            queue.append((r,c))
            count = 1

            directions = [
                (1,0),
                (-1,0),
                (0,1),
                (0,-1)
            ]
            while queue:
                curr_r, curr_c = queue.popleft()

                for x, y in directions:
                    nr, nc = curr_r + x, curr_c + y
                    if 0 <= nr < row and 0 <= nc < col and (nr, nc) not in seen and grid[nr][nc] == 1:
                        seen.add((nr,nc))
                        queue.append((nr,nc))
                        count += 1

            return count
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and (i, j) not in seen:
                    max_count = max(max_count, bfs(i,j))

        return max_count
        
    
