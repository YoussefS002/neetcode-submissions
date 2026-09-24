class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res=None
        max_occ=0
        h={}
        for num in nums:
            h[num]=h.get(num, 0)+1
            if h[num]>max_occ:
                res=num
                max_occ=h[num]
        return res