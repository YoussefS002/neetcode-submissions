class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h={}
        for num in nums:
            h[num]=h.get(num, 0)+1
        L=[(-h[x], x) for x in h.keys()]
        heapq.heapify(L)
        res=[]
        for i in range(k):
            res.append(heapq.heappop(L)[1])
        return res
        