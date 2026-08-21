class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        dp=[[None for j in range(len(points[0]))] for i in range(len(points))]
        for j in range(len(points[0])):
            dp[0][j]=points[0][j]
        for i in range(1, len(points)):
            for j in range(len(points[0])):
                dp[i][j]=points[i][j]+max([dp[i-1][k]-abs(j-k) for k in range(len(points[0]))])
        return max(dp[-1])