class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        frq={}
        res=0
        s=0
        for i in range(len(nums)):
            s+=nums[i]
            over=s-k
            if over==0:
                res+=1
            if over in frq:
                res+=frq[over]
            frq[s]=frq.get(s, 0)+1
        return res