class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        h={}
        res=0
        for num in nums:
            if num-1 in h:
                h[num]=h[num-1]+1
            else:
                h[num]=1
            res=max(res, h[num])
        return res