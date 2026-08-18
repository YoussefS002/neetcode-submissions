class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = [(i, 0) for i in range(-1000, 1001)]
        for num in nums:
            d[num+1000] = (d[num+1000][0], d[num+1000][1]+1) 
        d = sorted(d, reverse=True, key=lambda x:x[1]) # O(1)
        return [x[0] for x in d[:k]]

        