# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(rootA, rootB):
            if not rootA and not rootB:
                return True
            if not rootA or not rootB:
                return False
            if rootA.val != rootB.val:
                return False
            return isSameTree(rootA.left, rootB.left) and isSameTree(rootA.right, rootB.right)
        queue=deque([root])
        while queue:
            node=queue.popleft()
            if isSameTree(node, subRoot):
                return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return False