class Solution:
    def solve(self, board: List[List[str]]) -> None:
        NB_ROWS=len(board)
        NB_COLS=len(board[0])
        vis=[[False for j in range(NB_COLS)] for i in range(NB_ROWS)]
        def dfs(i, j):
            if vis[i][j]:
                return
            vis[i][j]=True
            directions=[(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
            for (x, y) in directions:
                if 0<=x<NB_ROWS and 0<=y<NB_COLS:
                    if board[x][y]=='O':
                        dfs(x, y)
        for i in range(NB_ROWS):
            if board[i][0]=='O':
                dfs(i, 0)
            if board[i][NB_COLS-1]=='O':
                dfs(i, NB_COLS-1)
        for j in range(NB_COLS):
            if board[0][j]=='O':
                dfs(0, j)
            if board[NB_ROWS-1][j]=='O':
                dfs(NB_ROWS-1, j)
        for i in range(NB_ROWS):
            for j in range(NB_COLS):
                if board[i][j]=='O':
                    if not vis[i][j]:
                        board[i][j]='X'