class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist={k:0}
        def dfs(i, d):
            for u, v, t in times:
                if u==i:
                    if d+t < dist.get(v, float('inf')):
                        dist[v]=d+t
                        dfs(v, dist[v])
        dfs(k, 0)
        if len(dist)<n:
            return -1
        
        return max([y for x, y in dist.items()])
