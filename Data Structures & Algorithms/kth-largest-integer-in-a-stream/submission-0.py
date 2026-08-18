class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        heapq.heapify_max(nums)
        self.nums=nums

    def add(self, val: int) -> int:
        heapq.heappush_max(self.nums, val)
        k_first=[]
        for i in range(self.k):
            k_first.append(heapq.heappop_max(self.nums))
        res=k_first[-1]
        for i in range(self.k-1, -1, -1):
            heapq.heappush_max(self.nums, k_first[i])
        return res
        