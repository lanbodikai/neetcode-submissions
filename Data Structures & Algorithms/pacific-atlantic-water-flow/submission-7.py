class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row, col = len(heights), len(heights[0])

        pacific = set()
        atlantic = set()


        def bfs(starts, visited):
            queue = deque(starts)

            for r, c in starts:
                visited.add((r,c))

            directions= [
                (0, 1),
                (0, -1),
                (1, 0),
                (-1, 0),
            ]
            while queue:
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = dr+r, dc+c

                    if (nr < 0 or nr >= row or
                        nc < 0 or nc >= col or
                        (nr, nc) in visited
                    ):
                        continue

                    if heights[nr][nc] >= heights[r][c]:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            
        atlantic_starts = []
        pacific_starts = []

        for r in range(row):
            pacific_starts.append((r, 0))
            atlantic_starts.append((r, col - 1))

        for c in range(col):
            pacific_starts.append((0, c))
            atlantic_starts.append((row - 1, c))

        bfs(pacific_starts, pacific)
        bfs(atlantic_starts, atlantic)
        
        result = []
        for r in range(row):
            for c in range(col):
                if (r,c) in pacific and (r,c) in atlantic:
                    result.append([r,c])
        return result
