class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum=[]
        for num in nums:
            if prefix_sum:
                prefix_sum.append(num+prefix_sum[-1])
            else:
                prefix_sum.append(num)
        h={0:1}
        res=0
        for ps in prefix_sum:
            target=ps-k
            res+=h.get(target, 0)
            h[ps]=h.get(ps, 0)+1
        return res