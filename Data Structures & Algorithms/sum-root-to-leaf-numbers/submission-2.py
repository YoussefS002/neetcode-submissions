# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        nums=[]
        def dfs(root, cur):
            if (not root.right) and (not root.left):
                nums.append(int("".join(cur)))
                return
            if root.left:
                dfs(root.left, cur+[str(root.left.val)])
            if root.right:
                dfs(root.right, cur+[str(root.right.val)])
        dfs(root, [str(root.val)])
        return sum(nums)