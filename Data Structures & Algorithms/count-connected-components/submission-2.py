class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ma = defaultdict(list)

        for i, e in edges:
            ma[i].append(e)
            ma[e].append(i)

        count = 0

        seen = set()
        def dfs(node):
            seen.add(node)

            
            for n in ma[node]:
                if n not in seen:
                    dfs(n)
 
        for i in range(n):
            if i not in seen:
                count += 1
                dfs(i)
        
        return count
            