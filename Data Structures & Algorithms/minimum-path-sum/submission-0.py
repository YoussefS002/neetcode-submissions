class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        sums=[[0 for j in range(len(grid[0]))] for i in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i>0 and j>0:
                    sums[i][j]=grid[i][j]+min(sums[i-1][j], sums[i][j-1])
                elif i==0:
                    sums[i][j]=grid[i][j]+sums[i][j-1]
                elif j==0:
                    sums[i][j]=grid[i][j]+sums[i-1][j]
                else:
                    sums[i][j]=grid[i][j]
        return sums[-1][-1]