# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_same(A, B):
            if not A or not B:
                return not A and not B
            if A.val!=B.val:
                return False
            return is_same(A.left, B.left) and is_same(A.right, B.right)
        stack=[root]
        while stack:
            node=stack.pop()
            if is_same(node, subRoot):
                return True
            if node:
                stack.append(node.left)
                stack.append(node.right)
        return False