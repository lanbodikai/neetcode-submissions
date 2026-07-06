class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        mam = defaultdict(list)
        for node1, node2 in edges:
            mam[node1].append(node2)
            mam[node2].append(node1)

        visited = set()
        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)

            for nex in mam[node]:
                if nex == parent:
                    continue
                
                if not dfs(nex, node):
                    return False
            
            return True

        

        if not dfs(0, None):
            return False

        return len(visited) == n