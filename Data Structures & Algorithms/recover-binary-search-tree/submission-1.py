# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def inorder(root):
            if not root:
                return []
            return inorder(root.left)+[root.val]+inorder(root.right)
        L=inorder(root)
        swapped=[None, None]
        for i in range(1, len(L)):
            if L[i]<L[i-1]:
                if not swapped[0]:
                    swapped[0]=L[i-1]
                    swapped[1]=L[i]
                else:
                    swapped[1]=L[i]

        def invert(root, a, b):
            if not root:
                return None
            if root.val==a:
                root.val=b
            elif root.val==b:
                root.val=a
            invert(root.left, a, b)
            invert(root.right, a, b)
        invert(root, swapped[0], swapped[1])
        