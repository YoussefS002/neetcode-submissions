class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp=[[None for j in range(366)] for i in range(len(days))]
        def dfs(i, end):
            if i==len(days):
                return 0
            if dp[i][end] is not None:
                return dp[i][end]
            include=dfs(i+1, end) if days[i]<=end else float("inf")
            buy1=costs[0] + dfs(i+1, min(days[i], 365))
            buy2=costs[1] + dfs(i+1, min(days[i]+6, 365))
            buy3=costs[2] + dfs(i+1, min(days[i]+29, 365))
            dp[i][end] = min([include, buy1, buy2, buy3])
            return dp[i][end]
        return dfs(0, 0)
    