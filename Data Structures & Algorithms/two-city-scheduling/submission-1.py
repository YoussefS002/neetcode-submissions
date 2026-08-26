class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diff=[(costs[i][0]-costs[i][1], i) for i in range(len(costs))]
        diff.sort()
        A=set()
        B=set()
        for i in range(len(diff)):
            if i<len(diff)//2:
                A.add(diff[i][1])
            else:
                B.add(diff[i][1])
        res=0
        for a in A:
            res+=costs[a][0]
        for b in B:
            res+=costs[b][1]
        return res
