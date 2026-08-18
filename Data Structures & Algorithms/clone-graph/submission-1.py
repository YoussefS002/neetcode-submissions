"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clones={}
        def aux(node):
            if not node:
                return None
            if node in clones:
                return clones[node]
            clone = Node(node.val)
            clones[node]=clone
            for ng in node.neighbors:
                ng_clone=aux(ng)
                clone.neighbors.append(ng_clone)
            return clone
        return aux(node)