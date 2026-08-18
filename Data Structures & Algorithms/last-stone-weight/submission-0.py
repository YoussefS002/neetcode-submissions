class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones)>1:
            first=heapq.heappop_max(stones)
            second=heapq.heappop_max(stones)
            heapq.heappush_max(stones, first-second)
        return stones[0]