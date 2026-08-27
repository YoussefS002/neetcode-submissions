"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def topleft(grid):
            n=len(grid)
            return [
                grid[i][:n//2] for i in range(n//2)
            ]
        def topright(grid):
            n=len(grid)
            return [
                grid[i][n//2:] for i in range(n//2)
            ]
        def bottomleft(grid):
            n=len(grid)
            return [
                grid[i][:n//2] for i in range(n//2, n)
            ]
        def bottomright(grid):
            n=len(grid)
            return [
                grid[i][n//2:] for i in range(n//2, n)
            ]
        def hasuniqueval(grid):
            val=grid[0][0]
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j]!=val:
                        return False
            return True
        if hasuniqueval(grid):
            return Node(val=grid[0][0]==1, isLeaf=True)
        node=Node()
        n=len(grid)
        node.topLeft=self.construct(topleft(grid))
        node.topRight=self.construct(topright(grid))
        node.bottomLeft=self.construct(bottomleft(grid))
        node.bottomRight=self.construct(bottomright(grid))
        return node


