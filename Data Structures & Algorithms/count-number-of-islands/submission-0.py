class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        NB_ROWS=len(grid)
        NB_COLS=len(grid[0])
        vis=[[False for j in range(NB_COLS)] for i in range(NB_ROWS)]
        def dfs(i, j):
            # marks as visited all ones that can be accessed from i,j
            if not 0<=i<NB_ROWS:
                return
            if not 0<=j<NB_COLS:
                return
            if grid[i][j]=="0":
                return
            if vis[i][j]:
                return
            vis[i][j]=True
            for k,l in ((-1,0), (1,0), (0,-1), (0,1)):
                dfs(i+k, j+l)

        count=0
        for i in range(NB_ROWS):
            for j in range(NB_COLS):
                if grid[i][j]=="1" and not vis[i][j]:
                    count+=1
                    dfs(i,j)
        return count
