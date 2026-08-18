# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def isCommonAncestor(x, p, q):
            stack=[x]
            vis=set()
            while stack:
                node=stack.pop()
                vis.add(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            return p.val in vis and q.val in vis
        if root.left and isCommonAncestor(root.left, p, q):
            return self.lowestCommonAncestor(root.left, p, q)
        if root.right and isCommonAncestor(root.right, p, q):
            return self.lowestCommonAncestor(root.right, p, q)
        return root