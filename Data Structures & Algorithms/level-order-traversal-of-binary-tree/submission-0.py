# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = {}
        def dfs(x, level):
            if not x:
                return
            levels[x]=level
            dfs(x.left, level+1)
            dfs(x.right, level+1)
        dfs(root, 0)
        queue=deque([root]) if root else None
        level=-1
        res=[]
        while queue:
            node=queue.popleft()
            if levels[node] != level:
                level=levels[node]
                res.append([node.val])
            else:
                res[-1].append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res