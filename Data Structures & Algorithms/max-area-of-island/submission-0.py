class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res=0
        vis=[[False for j in range(len(grid[0]))] for i in range(len(grid))]
        def dfs(i, j, nb):
            if i<0 or i>=len(grid):
                return nb
            if j<0 or j >=len(grid[0]):
                return nb
            if grid[i][j]==0:
                return nb
            if vis[i][j]:
                return nb
            vis[i][j]=True
            dirs=[(i+1, j), (i-1, j), (i, j-1), (i, j+1)]
            nb+=1
            for k, l in dirs:
                nb=dfs(k,l,nb)
            return nb
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1 and not vis[i][j]:
                    res=max(res, dfs(i, j, 0))
        return res