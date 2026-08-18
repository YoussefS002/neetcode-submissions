# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def nbTreeElements(root, baseNumber, res):
            if not root:
                return baseNumber, res
            elif not root.left and not root.right:
                if baseNumber+1==k:
                    return baseNumber+1, root.val
                return baseNumber+1, res
            else:
                nbLeftElements, res =nbTreeElements(root.left, baseNumber, res)
                nbRightElements, res=nbTreeElements(root.right, nbLeftElements+1, res)
                if nbLeftElements+1==k:
                    return nbRightElements, root.val
                return nbRightElements, res

        nb, res= nbTreeElements(root, 0, None)
        return res
            