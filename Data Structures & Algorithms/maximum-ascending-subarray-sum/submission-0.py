class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        l,r=0,0
        s=nums[l]
        res=s
        while r<len(nums):
            if r+1<len(nums) and nums[r+1]>nums[r]:
                s+=nums[r+1]
                r+=1
                res=max(res, s)
            else:
                l=r+1
                r=r+1
                if l<len(nums):
                    s=nums[l]
                    res=max(res, s)
        return res