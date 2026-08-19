# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = deque([root])

        #start with default root push queue, for each element in queue scan if has left and right, pop it and push temp, if yes, push queue,

        while queue:
            temp = []
            count = len(queue)

            for i in range(count):      
                a = queue.popleft()
                temp.append(a.val)

                if a.left:
                    queue.append(a.left)

                if a.right:
                    queue.append(a.right)
            
            res.append(temp)
        
        return res
