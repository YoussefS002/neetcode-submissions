class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        l, r = 0, 0
        res=0
        while l<len(nums):
            if r<len(nums) and nums[l]+nums[r]<=target:
                res+=pow(2, max(0, r-l-1))
                r+=1
                
            else:
                l=l+1
                r=l
        return res%1000000007


            