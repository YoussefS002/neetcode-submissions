# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def aux(root, mini=-float("inf"), maxi=float("inf")):
            if not root:
                return True
            if not mini < root.val < maxi:
                return False 
            if root.left and root.left.val >= root.val:
                return False
            if root.right and root.right.val <= root.val:
                return False
            return aux(root.left, mini=mini, maxi=root.val) and aux(root.right, mini=root.val, maxi=maxi)
        return aux(root)