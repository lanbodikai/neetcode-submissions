class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        temp = []

        queue = deque(nums)

        def dfs():
            if len(temp) == len(nums):
                res.append(temp.copy())
                return
            
            for _ in range(len(queue)):
                q = queue.popleft()
                temp.append(q)

                dfs()

                temp.pop()
                queue.append(q)
        dfs()

        return res

            