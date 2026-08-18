# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        parent = {}
        stack = [root]
        while stack:
            node=stack.pop()
            if node.left:
                parent[node.left.val]=node
                stack.append(node.left)
            if node.right:
                parent[node.right.val]=node
                stack.append(node.right)
        pAncestors={p.val}
        while p.val!=root.val:
            p=parent[p.val]
            pAncestors.add(p.val)
        while (q.val != root.val) and (q.val not in pAncestors):
            q=parent[q.val]
        return q

